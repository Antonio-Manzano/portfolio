import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import date, timedelta

# Configuración de la página
st.set_page_config(page_title="Financial Data Dashboard", layout="wide")
st.title("📈 Análisis Cuantitativo de Activos Financieros")
st.write("Dashboard interactivo para el análisis de series temporales y medias móviles.")

# Barra lateral para inputs del usuario
st.sidebar.header("Parámetros del Modelo")
ticker_symbol = st.sidebar.text_input("Ticker del Activo (ej. AAPL, SPY, TSLA)", "AAPL")
start_date = st.sidebar.date_input("Fecha de inicio", date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("Fecha de fin", date.today())

# Descarga de datos usando yfinance
@st.cache_data # Esto optimiza la velocidad para no recargar datos a cada rato
def load_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Descargando datos financieros...')
data = load_data(ticker_symbol, start_date, end_date)
data_load_state.text('¡Datos cargados exitosamente!')

# Mostrar tabla de datos en crudo (opcional)
if st.checkbox('Mostrar datos en crudo (Raw Data)'):
    st.subheader('Datos Financieros Históricos')
    st.write(data.tail())

# Cálculos estadísticos: Medias Móviles (Pandas en acción)
if not data.empty:
    # yfinance a veces devuelve multi-índices, aseguramos tomar la columna correcta
    close_col = 'Close' if 'Close' in data.columns else data.columns[4] 
    
    data['MA50'] = data[close_col].rolling(window=50).mean()
    data['MA200'] = data[close_col].rolling(window=200).mean()

    # Creación del gráfico interactivo con Plotly
    st.subheader(f'Gráfico de Velas y Medias Móviles para {ticker_symbol.upper()}')
    
    fig = go.Figure()
    
    # Velas japonesas
    fig.add_trace(go.Candlestick(x=data['Date'],
                    open=data['Open'].squeeze(),
                    high=data['High'].squeeze(),
                    low=data['Low'].squeeze(),
                    close=data['Close'].squeeze(),
                    name='Precio'))
    
    # Líneas de Media Móvil
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA50'], line=dict(color='blue', width=1.5), name='Media Móvil 50 días'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA200'], line=dict(color='red', width=1.5), name='Media Móvil 200 días'))
    
    fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("No se encontraron datos para este Ticker en las fechas seleccionadas.")