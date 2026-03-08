import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(page_title="Simulación Montecarlo", layout="wide")
st.title("🎲 Simulación de Montecarlo: Riesgo y Predicción")
st.write("""
Este modelo utiliza el **Movimiento Browniano Geométrico** para simular miles de posibles trayectorias 
futuras para el precio de un activo, basándose en su volatilidad histórica.
""")

# ==========================================
# PARÁMETROS DEL USUARIO
# ==========================================
st.sidebar.header("Parámetros de la Simulación")
ticker_symbol = st.sidebar.text_input("Ticker del Activo (ej. SPY, AAPL)", "SPY").upper().strip()
dias_simulacion = st.sidebar.slider("Días a simular hacia el futuro", min_value=10, max_value=252, value=30)
num_simulaciones = st.sidebar.slider("Número de escenarios (trayectorias)", min_value=100, max_value=5000, value=1000, step=100)

if not ticker_symbol:
    st.warning("⚠️ Ingresa un Ticker para comenzar.")
    st.stop()

# ==========================================
# DESCARGA DE DATOS HISTÓRICOS (1 año hacia atrás)
# ==========================================
@st.cache_data
def get_historical_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1y")
        return data['Close']
    except Exception:
        return pd.Series(dtype='float64')

with st.spinner('Descargando historial para calcular volatilidad...'):
    precios = get_historical_data(ticker_symbol)

if precios.empty:
    st.error(f"❌ No se encontraron datos para '{ticker_symbol}'.")
    st.stop()

# ==========================================
# MATEMÁTICAS DEL MODELO (NUMPY EN ACCIÓN)
# ==========================================
# 1. Calcular retornos logarítmicos diarios
retornos_log = np.log(1 + precios.pct_change()).dropna()

# 2. Calcular Drift (Tendencia) y Volatilidad (Desviación Estándar)
u = retornos_log.mean()
var = retornos_log.var()
drift = u - (0.5 * var)
stdev = retornos_log.std()

# 3. Preparar la matriz de simulación (Días x Simulaciones)
# Aquí usamos NumPy para generar miles de números aleatorios con distribución normal al instante
Z = np.random.normal(0, 1, (dias_simulacion, num_simulaciones))
retornos_diarios_simulados = np.exp(drift + stdev * Z)

# 4. Generar las trayectorias de precios
# Creamos una matriz llena de ceros y asignamos el último precio real al día 0
price_paths = np.zeros_like(retornos_diarios_simulados)
precio_actual = precios.iloc[-1]
price_paths[0] = precio_actual

# Bucle para calcular el precio acumulado día con día
for t in range(1, dias_simulacion):
    price_paths[t] = price_paths[t-1] * retornos_diarios_simulados[t]

st.success(f"¡Simulación completada! Se calcularon {num_simulaciones} escenarios para los próximos {dias_simulacion} días.")

# ==========================================
# VISUALIZACIÓN DE RESULTADOS
# ==========================================
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Trayectorias Simuladas para {ticker_symbol}")
    # Para no saturar el navegador, graficamos un máximo de 200 líneas
    lineas_a_graficar = min(200, num_simulaciones)
    
    fig_paths = go.Figure()
    for i in range(lineas_a_graficar):
        fig_paths.add_trace(go.Scatter(y=price_paths[:, i], mode='lines', line=dict(width=1, color='rgba(0, 100, 255, 0.1)'), showlegend=False))
    
    # Línea del precio inicial
    fig_paths.add_trace(go.Scatter(x=[0, dias_simulacion], y=[precio_actual, precio_actual], mode='lines', name='Precio Actual', line=dict(color='red', width=2, dash='dash')))
    
    fig_paths.update_layout(height=400, template="plotly_white", xaxis_title="Días hacia el futuro", yaxis_title="Precio Simulado ($)")
    st.plotly_chart(fig_paths, use_container_width=True)

with col2:
    st.subheader("Análisis de Riesgo (Percentiles)")
    
    # Extraemos los precios finales de todas las simulaciones
    precios_finales = price_paths[-1]
    
    # Calculamos percentiles (Value at Risk)
    p_95 = np.percentile(precios_finales, 95)
    p_50 = np.percentile(precios_finales, 50)
    p_5 = np.percentile(precios_finales, 5)
    
    st.metric(label="Precio Actual", value=f"${precio_actual:.2f}")
    st.markdown("---")
    st.metric(label="Mejor Escenario (Percentil 95%)", value=f"${p_95:.2f}", delta=f"{((p_95/precio_actual)-1)*100:.2f}%")
    st.metric(label="Escenario Esperado (Mediana 50%)", value=f"${p_50:.2f}", delta=f"{((p_50/precio_actual)-1)*100:.2f}%")
    st.metric(label="Peor Escenario (Percentil 5%)", value=f"${p_5:.2f}", delta=f"{((p_5/precio_actual)-1)*100:.2f}%")

    st.info("💡 **Nota Actuarial:** El Percentil 5% representa el 'Value at Risk' (VaR). Significa que, con un 95% de confianza, el precio no caerá por debajo de este nivel.")
