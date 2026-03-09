import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import cv2
import joblib
import os
import gdown
from datetime import date, timedelta
from streamlit_drawable_canvas import st_canvas

# ========================
# Configuración de la app
# ========================
st.set_page_config(
    page_title="Portfolio | Juan Antonio Manzano",
    layout="wide"
)

# ========================
# Selector de idioma
# ========================
language = st.sidebar.selectbox("Select Language / Selecciona Idioma", ["English", "Español"])

# ========================
# Tabs principales
# ========================
tab_home, tab_github, tab_emnist, tab_montecarlo, tab_series = st.tabs(
    ["Home", "GitHub Proyects", "EMNIST", "Monte Carlo", "Time Series"]
)

# ========================
# PÁGINA DE INICIO
# ========================
with tab_home:
    if language == "English":
        st.title("Juan Antonio Manzano Ceja")
        st.subheader("Information Technology Engineering Student")
        st.markdown("""
Information Technology Engineering student at Universidad Politécnica de Victoria with a strong interest in 
software development, data systems, and computational problem solving.

My work focuses on applying programming, database design, and algorithmic logic to build reliable 
software solutions and analytical tools. I have experience working with Python, C++, SQL, and modern 
development tools to design systems that manage and analyze information efficiently.
""")
        st.markdown("### Areas of Focus")
        st.markdown("""
- Software development and algorithm design  
- Data analysis and computational modeling  
- Database architecture and optimization  
- Backend systems and API development  
- Applied statistics and machine learning
""")
        st.markdown("### Technical Stack")
        st.markdown("""
**Programming**

Python  
C++  
Java  
SQL  

**Data and Analytics**

Pandas  
NumPy  
Scikit-learn  
Statsmodels  
Plotly  

**Tools**

Git  
GitHub  
Linux  
Trello  
Jira
""")
        st.markdown("### Experience")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
**Robotics Instructor and Project Coordinator**  
Centro Estatal de Tecnología Educativa  
2024 – 2025

- Delivered introductory robotics courses focused on computational logic and programming fundamentals.
- Mentored students through hands-on robotics projects and STEM activities.
- Coordinated curriculum development and task management using agile methodologies.
""")
        with col2:
            st.markdown("""
**IT Support Technician**  
Escuela Secundaria General No. 7  
Feb 2021 – Aug 2021

- Maintained and supported more than 30 computer workstations.
- Diagnosed hardware and software issues within laboratory environments.
- Designed and deployed a CCTV surveillance system including cabling and configuration.
""")
        st.markdown("### About This Portfolio")
        st.markdown("""
This portfolio presents several projects where I apply programming, data analysis, and 
computational logic to real technical problems.

The applications shown here were primarily developed in Python and demonstrate work related to:

- Data analysis and visualization
- Algorithm implementation
- Database design
- Computational modeling
- Software system development

Use the navigation panel on the left to explore the projects and interact with the applications.
""")
        st.markdown("**Contact**")
        st.markdown("Email: gracetimesant@gmail.com  \nLinkedIn: linkedin.com/in/antonio-manzano-c")
    else:
        st.title("Juan Antonio Manzano Ceja")
        st.subheader("Estudiante de Ingeniería en Tecnologías de la Información")
        st.markdown("""
Estudiante de Ingeniería en Tecnologías de la Información en la Universidad Politécnica de Victoria, con interés en
desarrollo de software, sistemas de datos y resolución computacional de problemas.

Mi trabajo se enfoca en aplicar programación, diseño de bases de datos y lógica algorítmica para construir
soluciones de software confiables y herramientas analíticas.
""")
        st.markdown("### Áreas de Enfoque")
        st.markdown("""
- Desarrollo de software y diseño de algoritmos  
- Análisis de datos y modelado computacional  
- Arquitectura y optimización de bases de datos  
- Sistemas backend y desarrollo de APIs  
- Estadística aplicada y machine learning
""")
        st.markdown("### Stack Técnico")
        st.markdown("""
**Programación**

Python  
C++  
Java  
SQL  

**Datos y Análisis**

Pandas  
NumPy  
Scikit-learn  
Statsmodels  
Plotly  

**Herramientas**

Git  
GitHub  
Linux  
Trello  
Jira
""")
        st.markdown("### Experiencia")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
**Instructor de Robótica y Coordinador de Proyectos**  
Centro Estatal de Tecnología Educativa  
2024 – 2025

- Impartió cursos introductorios de robótica y lógica computacional.
- Guió a estudiantes en proyectos prácticos de robótica y actividades STEM.
- Coordinó desarrollo de currículo y gestión de tareas con metodologías ágiles.
""")
        with col2:
            st.markdown("""
**Técnico de Soporte en IT**  
Escuela Secundaria General No. 7  
Feb 2021 – Ago 2021

- Mantenimiento y soporte de más de 30 computadoras.
- Diagnóstico de problemas de hardware y software en laboratorios.
- Diseño e implementación de sistema de CCTV incluyendo cableado y configuración.
""")
        st.markdown("### Sobre Este Portafolio")
        st.markdown("""
Este portafolio presenta proyectos donde aplico programación, análisis de datos y
lógica computacional a problemas técnicos reales.

Las aplicaciones mostradas fueron desarrolladas principalmente en Python y demuestran trabajos relacionados con:

- Análisis y visualización de datos
- Implementación de algoritmos
- Diseño de bases de datos
- Modelado computacional
- Desarrollo de sistemas de software

Usa el panel de navegación a la izquierda para explorar los proyectos e interactuar con las aplicaciones.
""")
        st.markdown("**Contacto**")
        st.markdown("Email: gracetimesant@gmail.com  \nLinkedIn: linkedin.com/in/antonio-manzano-c")


with tab_github:
    if language == "English":
        st.markdown("### Projects")
    else:
        st.markdown("### Proyectos")
    
    # ==========================================
    # Project 1: Edulibreria
    # ==========================================
    with st.expander("Edulibreria | Advanced Data Structures in C++", expanded=False if language=="Español" else True):
        col1, col2 = st.columns([2,1])
        with col1:
            if language=="English":
                st.markdown("""
    **Academic Objective:** Understand memory management and implement complex data structures manually without high-level libraries.
    
    **Technical Development:**
    - **Implementation:** Inventory management software in pure C++.
    - **Algorithms:** Trees and linked lists for efficient search, insertion, and deletion.
    - **Optimization:** Reduce computational overhead by structuring data logically.
    """)
            else:
                st.markdown("""
    **Objetivo Académico:** Comprender el manejo de memoria e implementar estructuras de datos complejas sin librerías de alto nivel.
    
    **Desarrollo Técnico:**
    - **Implementación:** Software de gestión de inventario en C++ puro.
    - **Algoritmia:** Árboles y listas enlazadas para búsqueda, inserción y eliminación.
    - **Optimización:** Reducción del overhead computacional mediante estructuración lógica de los datos.
    """)
        with col2:
            st.info("Concepts: C++, Memory Management, Algorithmic Complexity")
            st.button("View on GitHub", key="edulibreria", on_click=lambda: st.experimental_set_query_params(url="https://github.com/TU_USUARIO/edulibreria"))
    
    # ==========================================
    # Project 2: Iticritics
    # ==========================================
    with st.expander("Iticritics | Relational Database Design (SQL)"):
        col1, col2 = st.columns([2,1])
        with col1:
            if language=="English":
                st.markdown("""
    **Academic Objective:** Design a normalized database architecture and integrate with a backend server.
    
    **Technical Development:**
    - **Data Modeling:** Robust relational schemas for users, reviews, and metadata.
    - **Queries:** Optimize queries for low-latency data retrieval.
    - **Backend Integration:** Node.js + JavaScript for server logic.
    """)
            else:
                st.markdown("""
    **Objetivo Académico:** Diseñar arquitectura de base de datos normalizada e integrarla con un backend.
    
    **Desarrollo Técnico:**
    - **Modelado de Datos:** Esquemas relacionales robustos (SQL) para usuarios, reseñas y metadatos.
    - **Consultas:** Optimización de queries para baja latencia.
    - **Integración Backend:** Node.js + JavaScript para la lógica del servidor.
    """)
        with col2:
            st.info("Concepts: SQL Normalized, Node.js, Client-Server Architecture")
            st.button("View on GitHub", key="iticritics", on_click=lambda: st.experimental_set_query_params(url="https://github.com/TU_USUARIO/iticritics"))
    
    # ==========================================
    # Project 3: Flooded
    # ==========================================
    with st.expander("Flooded | Full Stack & NoSQL Development"):
        col1, col2 = st.columns([2,1])
        with col1:
            if language=="English":
                st.markdown("""
    **Academic Objective:** Apply agile methodologies in building a MERN Stack platform focusing on scalability and data flexibility.
    
    **Technical Development:**
    - **Flexible Schemas:** MongoDB & Mongoose for unstructured or changing data.
    - **RESTful API:** Express.js endpoints for secure CRUD operations.
    - **Frontend:** React.js integration showing full data flow.
    """)
            else:
                st.markdown("""
    **Objetivo Académico:** Aplicar metodologías ágiles en una plataforma MERN, enfocándose en escalabilidad y flexibilidad de datos.
    
    **Desarrollo Técnico:**
    - **Esquemas Flexibles:** MongoDB & Mongoose para datos no estructurados o cambiantes.
    - **API RESTful:** Endpoints con Express.js para operaciones CRUD.
    - **Frontend:** Integración con React.js mostrando flujo completo de datos.
    """)
        with col2:
            st.info("Concepts: MongoDB (NoSQL), API Creation, React.js")
            st.button("View on GitHub", key="flooded", on_click=lambda: st.experimental_set_query_params(url="https://github.com/TU_USUARIO/flooded"))
# ========================
# EMNIST
# ========================
with tab_emnist:
    if language == "English":
        st.title("Optical Character Recognition: EMNIST Classification")
        draw_text = "Draw a character in the box:"
        run_button = "Run Models"
        analysis_text = "Ensemble Analysis"
    else:
        st.title("Reconocimiento Óptico: Clasificación EMNIST")
        draw_text = "Dibuja un caracter en el recuadro:"
        run_button = "Ejecutar Modelos"
        analysis_text = "Análisis del Ensamble"

    EMNIST_MAPPING = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt"
    col1, col2 = st.columns([1,2])
    with col1:
        st.subheader(draw_text)
        canvas_result = st_canvas(
            fill_color="black",
            stroke_width=20,
            stroke_color="white",
            background_color="black",
            height=280,
            width=280,
            drawing_mode="freedraw",
            key="canvas",
        )
        btn_predecir = st.button(run_button, type="primary", use_container_width=True)
        st.caption(f"Supported characters: {EMNIST_MAPPING}")
    with col2:
        st.subheader(analysis_text)
        st.info("Draw something and press the button to run models.")

# ========================
# MONTE CARLO
# ========================
with tab_montecarlo:
    if language == "English":
        st.title("Monte Carlo Simulation")
    else:
        st.title("Simulación Montecarlo")

    ticker_symbol = st.text_input("Ticker (ej. SPY, AAPL)", "SPY").upper().strip()
    dias_simulacion = st.slider("Days to simulate", 10, 252, 30)
    num_simulaciones = st.slider("Number of trajectories", 100, 5000, 1000, step=100)

    if ticker_symbol:
        @st.cache_data
        def get_historical_data(ticker):
            try:
                stock = yf.Ticker(ticker)
                data = stock.history(period="1y")
                return data['Close']
            except:
                return pd.Series(dtype='float64')

        precios = get_historical_data(ticker_symbol)

        if precios.empty:
            st.error(f"No data for '{ticker_symbol}'")
        else:
            retornos_log = np.log(1 + precios.pct_change()).dropna()
            u = retornos_log.mean()
            var = retornos_log.var()
            drift = u - 0.5*var
            stdev = retornos_log.std()
            Z = np.random.normal(0, 1, (dias_simulacion, num_simulaciones))
            retornos_diarios_simulados = np.exp(drift + stdev*Z)
            price_paths = np.zeros_like(retornos_diarios_simulados)
            precio_actual = precios.iloc[-1]
            price_paths[0] = precio_actual
            for t in range(1,dias_simulacion):
                price_paths[t] = price_paths[t-1]*retornos_diarios_simulados[t]

            col1, col2 = st.columns([2,1])
            with col1:
                st.subheader(f"Simulated Paths for {ticker_symbol}")
                fig_paths = go.Figure()
                for i in range(min(200, num_simulaciones)):
                    fig_paths.add_trace(go.Scatter(y=price_paths[:,i], mode='lines',
                                                   line=dict(width=1,color='rgba(0,100,255,0.1)')))
                fig_paths.add_trace(go.Scatter(x=[0,dias_simulacion], y=[precio_actual, precio_actual],
                                               mode='lines', line=dict(color='red', width=2, dash='dash')))
                fig_paths.update_layout(height=400, xaxis_title="Days", yaxis_title="Price", template="plotly_white")
                st.plotly_chart(fig_paths, use_container_width=True)
            with col2:
                st.subheader("Risk Analysis")
                precios_finales = price_paths[-1]
                p_95 = np.percentile(precios_finales, 95)
                p_50 = np.percentile(precios_finales, 50)
                p_5 = np.percentile(precios_finales, 5)
                st.metric("Current Price", f"${precio_actual:.2f}")
                st.metric("Best Scenario (P95)", f"${p_95:.2f}")
                st.metric("Expected Scenario (Median)", f"${p_50:.2f}")
                st.metric("Worst Scenario (P5 / VaR)", f"${p_5:.2f}")

# ========================
# SERIES TEMPORALES
# ========================
with tab_series:
    if language == "English":
        st.title("Time Series Analysis")
    else:
        st.title("Análisis de Series Temporales")

    ticker_symbol_ts = st.text_input("Ticker", "AAPL").upper().strip()
    start_date = st.date_input("Start Date", date.today()-timedelta(days=365))
    end_date = st.date_input("End Date", date.today())

    if ticker_symbol_ts and start_date < end_date:
        @st.cache_data
        def load_data(ticker,start,end):
            try:
                data = yf.download(ticker,start=start,end=end,progress=False)
                data.reset_index(inplace=True)
                if 'Date' in data.columns:
                    data['Date'] = pd.to_datetime(data['Date']).dt.tz_localize(None)
                return data
            except:
                return pd.DataFrame()

        data = load_data(ticker_symbol_ts,start_date,end_date)
        if data.empty:
            st.error("No data found")
        else:
            data['MA50'] = data['Close'].rolling(50).mean()
            data['MA200'] = data['Close'].rolling(200).mean()
            fig = go.Figure()
            fig.add_trace(go.Candlestick(x=data['Date'], open=data['Open'], high=data['High'],
                                         low=data['Low'], close=data['Close'], name='Price'))
            fig.add_trace(go.Scatter(x=data['Date'], y=data['MA50'], line=dict(color='blue',width=1.5), name='MA50'))
            fig.add_trace(go.Scatter(x=data['Date'], y=data['MA200'], line=dict(color='red',width=1.5), name='MA200'))
            fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_white")
            st.plotly_chart(fig,use_container_width=True)

