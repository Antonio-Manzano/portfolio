import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import date, timedelta

st.set_page_config(page_title="Análisis de Series Temporales", layout="wide")
st.title("Análisis Cuantitativo de Series Temporales")
st.markdown("""
**Caso de Estudio: Manipulación y Visualización de Datos Financieros**

Implementación de algoritmos para el procesamiento de grandes volúmenes de datos bursátiles históricos. Este dashboard demuestra el uso de **Pandas** para la extracción de métricas cuantitativas (como medias móviles) y la estructuración de datos en crudo para su análisis de tendencias.
""")

st.sidebar.header("Parámetros del Modelo")
ticker_symbol = st.sidebar.text_input("Ticker del Activo (ej. AAPL, SPY, TSLA)", "AAPL").upper().strip()
start_date = st.sidebar.date_input("Fecha de inicio", date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("Fecha de fin", date.today())

if not ticker_symbol:
    st.warning("Por favor, ingresa un símbolo (Ticker) para comenzar.")
    st.stop()

if start_date >= end_date:
    st.sidebar.error("La fecha de inicio debe ser anterior a la fecha de fin.")
    st.stop()

@st.cache_data
def load_data(ticker, start, end):
    try:
        start_str = start.strftime('%Y-%m-%d')
        end_str = end.strftime('%Y-%m-%d')
        data = yf.download(ticker, start=start_str, end=end_str, progress=False)
        if not data.empty:
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.droplevel(1)
            data.reset_index(inplace=True)
            if 'Date' in data.columns:
                data['Date'] = pd.to_datetime(data['Date']).dt.tz_localize(None)
        return data
    except Exception as e:
        st.error(f"Error técnico interno: {e}")
        return pd.DataFrame()

with st.spinner('Descargando datos financieros...'):
    data = load_data(ticker_symbol, start_date, end_date)

if not data.empty and 'Close' in data.columns:
    st.success('¡Datos cargados exitosamente!')
    
    if st.checkbox('Mostrar datos en crudo (Raw Data)'):
        st.subheader('Datos Financieros Históricos')
        st.write(data.tail())

    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()

    st.subheader(f'Gráfico de Velas y Medias Móviles para {ticker_symbol}')
    
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data['Date'],
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    name='Precio'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA50'], line=dict(color='blue', width=1.5), name='Media Móvil 50 días'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA200'], line=dict(color='red', width=1.5), name='Media Móvil 200 días'))
    
    fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error(f"No se encontraron datos para '{ticker_symbol}'. Es posible que el Ticker no exista o haya sido deslistado.")