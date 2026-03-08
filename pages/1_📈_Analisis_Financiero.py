import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import date, timedelta

# Configuración de la página (Debe ser el primer comando)
st.set_page_config(page_title="Análisis Financiero", layout="wide")
st.title("📈 Análisis Cuantitativo de Activos Financieros")
st.write("Dashboard interactivo para el análisis de series temporales y medias móviles.")

# Barra lateral para inputs del usuario
st.sidebar.header("Parámetros del Modelo")
# .upper().strip() asegura que si el usuario pone espacios o minúsculas, se corrija solo
ticker_symbol = st.sidebar.text_input("Ticker del Activo (ej. AAPL, SPY, TSLA)", "AAPL").upper().strip()
start_date = st.sidebar.date_input("Fecha de inicio", date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("Fecha de fin", date.today())

# ==========================================
# 🛑 VALIDACIONES DE ENTRADA
# ==========================================
if not ticker_symbol:
    st.warning("⚠️ Por favor, ingresa un símbolo (Ticker) para comenzar.")
    st.stop() # Detiene la ejecución del resto de la página

if start_date >= end_date:
    st.sidebar.error("❌ Error: La fecha de inicio debe ser anterior a la fecha de fin.")
    st.stop() # Detiene la ejecución
# ==========================================

# Descarga de datos usando yfinance
@st.cache_data
def load_data(ticker, start, end):
    try:
        # Convertimos las fechas a texto (YYYY-MM-DD) para mayor estabilidad
        start_str = start.strftime('%Y-%m-%d')
        end_str = end.strftime('%Y-%m-%d')
        
        # Usamos download que suele ser más robusto para rangos de fechas
        data = yf.download(ticker, start=start_str, end=end_str, progress=False)
        
        if not data.empty:
            # Aplanar Multi-índices si yfinance decide devolverlos
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.droplevel(1)
                
            data.reset_index(inplace=True)
            
            # Limpiamos la zona horaria
            if 'Date' in data.columns:
                data['Date'] = pd.to_datetime(data['Date']).dt.tz_localize(None)
        return data
    except Exception as e:
        st.error(f"Error técnico interno: {e}") # Esto nos dirá exactamente qué falló
        return pd.DataFrame()

with st.spinner('Descargando datos financieros...'):
    data = load_data(ticker_symbol, start_date, end_date)

# Verificamos si realmente descargó algo antes de hacer cálculos
if not data.empty and 'Close' in data.columns:
    st.success('¡Datos cargados exitosamente!')
    
    # Mostrar tabla de datos en crudo (opcional)
    if st.checkbox('Mostrar datos en crudo (Raw Data)'):
        st.subheader('Datos Financieros Históricos')
        st.write(data.tail())

    # Cálculos estadísticos: Medias Móviles
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()

    # Creación del gráfico interactivo con Plotly
    st.subheader(f'Gráfico de Velas y Medias Móviles para {ticker_symbol}')
    
    fig = go.Figure()
    
    # Velas japonesas
    fig.add_trace(go.Candlestick(x=data['Date'],
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    name='Precio'))
    
    # Líneas de Media Móvil
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA50'], line=dict(color='blue', width=1.5), name='Media Móvil 50 días'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA200'], line=dict(color='red', width=1.5), name='Media Móvil 200 días'))
    
    fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
else:
    # Este mensaje aparece si el ticker inventado no existe en Yahoo Finance
    st.error(f"❌ No se encontraron datos para '{ticker_symbol}'. Es posible que el Ticker no exista o haya sido deslistado.")
