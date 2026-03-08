import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Simulación Montecarlo", layout="wide")
st.title("Simulación Estocástica de Montecarlo y Cálculo de VaR")
st.markdown("""
**Caso de Estudio: Cómputo de Alto Rendimiento y Probabilidad**

Este modelo matemático aplica el **Movimiento Browniano Geométrico** para simular escenarios de riesgo e incertidumbre. Destaca la optimización computacional mediante el uso de **NumPy** para realizar operaciones de álgebra lineal sobre matrices masivas, generando miles de trayectorias estocásticas para el cálculo del Value at Risk (VaR).
""")

st.sidebar.header("Parámetros de la Simulación")
ticker_symbol = st.sidebar.text_input("Ticker del Activo (ej. SPY, AAPL)", "SPY").upper().strip()
dias_simulacion = st.sidebar.slider("Días a simular hacia el futuro", min_value=10, max_value=252, value=30)
num_simulaciones = st.sidebar.slider("Número de escenarios (trayectorias)", min_value=100, max_value=5000, value=1000, step=100)

if not ticker_symbol:
    st.warning("Ingresa un Ticker para comenzar.")
    st.stop()

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
    st.error(f"No se encontraron datos para '{ticker_symbol}'.")
    st.stop()

retornos_log = np.log(1 + precios.pct_change()).dropna()
u = retornos_log.mean()
var = retornos_log.var()
drift = u - (0.5 * var)
stdev = retornos_log.std()

Z = np.random.normal(0, 1, (dias_simulacion, num_simulaciones))
retornos_diarios_simulados = np.exp(drift + stdev * Z)

price_paths = np.zeros_like(retornos_diarios_simulados)
precio_actual = precios.iloc[-1]
price_paths[0] = precio_actual

for t in range(1, dias_simulacion):
    price_paths[t] = price_paths[t-1] * retornos_diarios_simulados[t]

st.success(f"Simulación completada: {num_simulaciones} escenarios para los próximos {dias_simulacion} días.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Trayectorias Simuladas para {ticker_symbol}")
    lineas_a_graficar = min(200, num_simulaciones)
    fig_paths = go.Figure()
    for i in range(lineas_a_graficar):
        fig_paths.add_trace(go.Scatter(y=price_paths[:, i], mode='lines', line=dict(width=1, color='rgba(0, 100, 255, 0.1)'), showlegend=False))
    fig_paths.add_trace(go.Scatter(x=[0, dias_simulacion], y=[precio_actual, precio_actual], mode='lines', name='Precio Actual', line=dict(color='red', width=2, dash='dash')))
    fig_paths.update_layout(height=400, template="plotly_white", xaxis_title="Días hacia el futuro", yaxis_title="Precio Simulado ($)")
    st.plotly_chart(fig_paths, use_container_width=True)

with col2:
    st.subheader("Análisis de Riesgo (Percentiles)")
    precios_finales = price_paths[-1]
    p_95 = np.percentile(precios_finales, 95)
    p_50 = np.percentile(precios_finales, 50)
    p_5 = np.percentile(precios_finales, 5)
    
    st.metric(label="Precio Actual", value=f"${precio_actual:.2f}")
    st.markdown("---")
    st.metric(label="Mejor Escenario (Percentil 95%)", value=f"${p_95:.2f}", delta=f"{((p_95/precio_actual)-1)*100:.2f}%")
    st.metric(label="Escenario Esperado (Mediana 50%)", value=f"${p_50:.2f}", delta=f"{((p_50/precio_actual)-1)*100:.2f}%")
    st.metric(label="Peor Escenario (Percentil 5%)", value=f"${p_5:.2f}", delta=f"{((p_5/precio_actual)-1)*100:.2f}%")

    st.info("El Percentil 5% representa el 'Value at Risk' (VaR). Con un 95% de confianza, el precio no caerá por debajo de este nivel.")