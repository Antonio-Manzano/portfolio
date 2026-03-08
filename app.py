# app.py
import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import joblib
import os
import cv2
import gdown
from datetime import date, timedelta
from streamlit_drawable_canvas import st_canvas
import plotly.graph_objects as go

# =======================
# CONFIGURACIÓN DE PÁGINA
# =======================
st.set_page_config(page_title="Portfolio | Juan Antonio Manzano", layout="wide")

# =======================
# SELECTOR DE IDIOMA
# =======================
idioma = st.selectbox("Language / Idioma", options=["English", "Español"], index=0)

# =======================
# TEXTOS INICIO
# =======================
inicio_textos = {
    "English": {
        "title": "Juan Antonio Manzano Ceja",
        "subtitle": "Information Technology Engineering Student",
        "intro": """Information Technology Engineering student at Universidad Politécnica de Victoria with a strong interest in 
software development, data systems, and computational problem solving.

My work focuses on applying programming, database design, and algorithmic logic to build reliable 
software solutions and analytical tools. I have experience working with Python, C++, SQL, and modern 
development tools to design systems that manage and analyze information efficiently.""",
        "areas": "Areas of Focus",
        "areas_list": [
            "Software development and algorithm design",
            "Data analysis and computational modeling",
            "Database architecture and optimization",
            "Backend systems and API development",
            "Applied statistics and machine learning"
        ],
        "stack": "Technical Stack",
        "stack_programming": ["Python", "C++", "Java", "SQL"],
        "stack_data": ["Pandas", "NumPy", "Scikit-learn", "Statsmodels", "Plotly"],
        "stack_tools": ["Git", "GitHub", "Linux", "Trello", "Jira"],
        "experience": "Experience",
        "experience_1_title": "Robotics Instructor and Project Coordinator",
        "experience_1_org": "Centro Estatal de Tecnología Educativa",
        "experience_1_time": "2024 – 2025",
        "experience_1_tasks": [
            "Delivered introductory robotics courses focused on computational logic and programming fundamentals.",
            "Mentored students through hands-on robotics projects and STEM activities.",
            "Coordinated curriculum development and task management using agile methodologies."
        ],
        "experience_2_title": "IT Support Technician",
        "experience_2_org": "Escuela Secundaria General No. 7",
        "experience_2_time": "Feb 2021 – Aug 2021",
        "experience_2_tasks": [
            "Maintained and supported more than 30 computer workstations.",
            "Diagnosed hardware and software issues within laboratory environments.",
            "Designed and deployed a CCTV surveillance system including cabling and configuration."
        ],
        "about_portfolio": "About This Portfolio",
        "about_text": """This portfolio presents several projects where I apply programming, data analysis, and 
computational logic to real technical problems.

The applications shown here were primarily developed in Python and demonstrate work related to:

- Data analysis and visualization
- Algorithm implementation
- Database design
- Computational modeling
- Software system development

Use the navigation panel on the left to explore the projects and interact with the applications.""",
        "contact": "Contact",
        "contact_info": "Email: gracetimesant@gmail.com  \nLinkedIn: linkedin.com/in/antonio-manzano-c"
    },
    "Español": {
        "title": "Juan Antonio Manzano Ceja",
        "subtitle": "Estudiante de Ingeniería en Tecnologías de la Información",
        "intro": """Estudiante de Ingeniería en Tecnologías de la Información en la Universidad Politécnica de Victoria con gran interés en 
desarrollo de software, sistemas de datos y resolución computacional de problemas.

Mi trabajo se centra en aplicar programación, diseño de bases de datos y lógica algorítmica para construir soluciones de software confiables y herramientas analíticas. Tengo experiencia con Python, C++, SQL y herramientas modernas de desarrollo para diseñar sistemas que gestionen y analicen información de manera eficiente.""",
        "areas": "Áreas de Especialización",
        "areas_list": [
            "Desarrollo de software y diseño de algoritmos",
            "Análisis de datos y modelado computacional",
            "Arquitectura y optimización de bases de datos",
            "Sistemas backend y desarrollo de APIs",
            "Estadística aplicada y machine learning"
        ],
        "stack": "Stack Técnico",
        "stack_programming": ["Python", "C++", "Java", "SQL"],
        "stack_data": ["Pandas", "NumPy", "Scikit-learn", "Statsmodels", "Plotly"],
        "stack_tools": ["Git", "GitHub", "Linux", "Trello", "Jira"],
        "experience": "Experiencia",
        "experience_1_title": "Instructor de Robótica y Coordinador de Proyectos",
        "experience_1_org": "Centro Estatal de Tecnología Educativa",
        "experience_1_time": "2024 – 2025",
        "experience_1_tasks": [
            "Dictó cursos introductorios de robótica enfocados en lógica computacional y fundamentos de programación.",
            "Asesoró a estudiantes en proyectos de robótica y actividades STEM.",
            "Coordinó desarrollo de currículo y gestión de tareas usando metodologías ágiles."
        ],
        "experience_2_title": "Técnico de Soporte IT",
        "experience_2_org": "Escuela Secundaria General No. 7",
        "experience_2_time": "Feb 2021 – Ago 2021",
        "experience_2_tasks": [
            "Mantenimiento y soporte de más de 30 estaciones de trabajo.",
            "Diagnóstico de problemas de hardware y software en laboratorios.",
            "Diseño e implementación de un sistema de CCTV incluyendo cableado y configuración."
        ],
        "about_portfolio": "Acerca de este Portafolio",
        "about_text": """Este portafolio presenta varios proyectos donde aplico programación, análisis de datos y 
lógica computacional a problemas técnicos reales.

Las aplicaciones aquí mostradas fueron desarrolladas principalmente en Python y demuestran trabajo relacionado con:

- Análisis y visualización de datos
- Implementación de algoritmos
- Diseño de bases de datos
- Modelado computacional
- Desarrollo de sistemas de software

Utiliza el panel de navegación a la izquierda para explorar los proyectos e interactuar con las aplicaciones.""",
        "contact": "Contacto",
        "contact_info": "Email: gracetimesant@gmail.com  \nLinkedIn: linkedin.com/in/antonio-manzano-c"
    }
}

# =======================
# TABS DE NAVEGACIÓN
# =======================
tab_home, tab_portafolio, tab_emnist, tab_montecarlo, tab_series = st.tabs([
    "Home", "Portfolio", "EMNIST", "Monte Carlo", "Time Series"
])

# =======================
# HOME PAGE
# =======================
with tab_home:
    st.title(inicio_textos[idioma]["title"])
    st.subheader(inicio_textos[idioma]["subtitle"])
    st.markdown(inicio_textos[idioma]["intro"])
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {inicio_textos[idioma]['areas']}")
        for area in inicio_textos[idioma]["areas_list"]:
            st.markdown(f"- {area}")
    with col2:
        st.markdown(f"### {inicio_textos[idioma]['stack']}")
        st.markdown("**Programming**")
        for lang in inicio_textos[idioma]["stack_programming"]:
            st.markdown(f"- {lang}")
        st.markdown("**Data & Analytics**")
        for lib in inicio_textos[idioma]["stack_data"]:
            st.markdown(f"- {lib}")
        st.markdown("**Tools**")
        for tool in inicio_textos[idioma]["stack_tools"]:
            st.markdown(f"- {tool}")

    st.divider()
    st.markdown(f"### {inicio_textos[idioma]['experience']}")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**{inicio_textos[idioma]['experience_1_title']}**  \n{inicio_textos[idioma]['experience_1_org']}  \n{inicio_textos[idioma]['experience_1_time']}")
        for task in inicio_textos[idioma]["experience_1_tasks"]:
            st.markdown(f"- {task}")
    with col2:
        st.markdown(f"**{inicio_textos[idioma]['experience_2_title']}**  \n{inicio_textos[idioma]['experience_2_org']}  \n{inicio_textos[idioma]['experience_2_time']}")
        for task in inicio_textos[idioma]["experience_2_tasks"]:
            st.markdown(f"- {task}")

    st.divider()
    st.markdown(f"### {inicio_textos[idioma]['about_portfolio']}")
    st.markdown(inicio_textos[idioma]["about_text"])
    st.divider()
    st.markdown(f"**{inicio_textos[idioma]['contact']}**  \n{inicio_textos[idioma]['contact_info']}")

# =======================
# TAB PORTFOLIO
# =======================
with tab_portafolio:
    st.title("Proyectos Académicos")
    st.markdown("""
Como estudiante de **Ingeniería en Tecnologías de la Información (ITI)**, he desarrollado proyectos 
enfocados en la comprensión profunda de algoritmos, bases de datos y arquitectura de software. 
Estos trabajos reflejan mi capacidad para trasladar la teoría computacional a código funcional.
""")
    st.divider()

    # Proyecto 1: Edulibreria
    with st.expander("Edulibreria | Estructuras de Datos Avanzadas en C++", expanded=True):
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
### Objetivo Académico
Comprender el manejo de memoria y la implementación manual de estructuras de datos complejas sin depender de librerías de alto nivel.

### Desarrollo Técnico
* Implementación: Desarrollo de un software de gestión de inventario utilizando C++ puro.
* Algoritmia: Programación de árboles y listas enlazadas para la búsqueda, inserción y eliminación eficiente de registros.
* Optimización: Reducción del overhead computacional al estructurar los datos de manera lógica.
""")
        with col2:
            st.info("Conceptos Clave:\n\n* C++\n* Manejo de Memoria\n* Complejidad Algorítmica")
            st.markdown("[Ver Código en GitHub](https://github.com/TU_USUARIO/edulibreria)")

    # Proyecto 2: Iticritics
    with st.expander("Iticritics | Diseño de Bases de Datos Relacionales (SQL)"):
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
### Objetivo Académico
Diseñar una arquitectura de base de datos normalizada e integrarla con un servidor backend para manejar flujos de información estructurada.

### Desarrollo Técnico
* Modelado de Datos: Creación de esquemas relacionales robustos (SQL) para gestionar perfiles de usuario, reseñas y metadatos.
* Consultas: Optimización de peticiones a la base de datos.
* Integración Backend: Uso de Node.js y JavaScript (ES6+) para construir la lógica del servidor.
""")
        with col2:
            st.info("Conceptos Clave:\n\n* SQL Normalizado\n* Node.js\n* Arquitectura Cliente-Servidor")
            st.markdown("[Ver Código en GitHub](https://github.com/TU_USUARIO/iticritics)")

    # Proyecto 3: Flooded
    with st.expander("Flooded | Desarrollo Full Stack y Bases de Datos NoSQL"):
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
### Objetivo Académico
Aplicar metodologías ágiles en la construcción de una plataforma integral (MERN Stack).

### Desarrollo Técnico
* Esquemas Flexibles: Diseño de base de datos utilizando MongoDB y Mongoose.
* API RESTful: Programación de endpoints con Express.js.
* Interfaz de Usuario: Conexión con un frontend dinámico en React.js.
""")
        with col2:
            st.info("Conceptos Clave:\n\n* MongoDB (NoSQL)\n* Creación de APIs\n* React.js")
            st.markdown("[Ver Código en GitHub](https://github.com/TU_USUARIO/flooded)")

# =======================
# TAB EMNIST
# =======================
with tab_emnist:
    st.title("Reconocimiento Óptico EMNIST")
    EMNIST_MAPPING = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt"

    # Cargar modelos
    @st.cache_resource
    def cargar_modelos():
        modelos = {}
        modelos_drive = {
            "modelo_3": "16yShYONQ7E_YpkuFQ1HiWNRSutGzhzIk", 
            "modelo_4": "1sg7TTVjqm6kPEDL6sUJn_6NWsTJdLWE1",
            "modelo_5": "1flP34CF0BS-7dU-Bmoxr0jTRIUYMSEC6", 
            "modelo_6": "17s7NiPtdOQ0D8S9K5eezYGlpJ51OWazV",
            "modelo_8": "1MmdfVGFtqYdCft3IEdY6vdKlr8ttUk_l"
        }
        carpeta = "clasificadores"
        os.makedirs(carpeta, exist_ok=True)
        for nombre, file_id in modelos_drive.items():
            ruta_local = os.path.join(carpeta, f"{nombre}.pkl")
            if not os.path.exists(ruta_local):
                gdown.download(id=file_id, output=ruta_local, quiet=False)
            modelos[nombre] = joblib.load(ruta_local)
        return modelos

    modelos = cargar_modelos()

    col1, col2 = st.columns([1,2])
    with col1:
        st.subheader("Lienzo de Dibujo")
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
        btn_predecir = st.button("Ejecutar Modelos", type="primary", use_container_width=True)
        st.caption(f"Caracteres soportados: {EMNIST_MAPPING}")

    with col2:
        st.subheader("Análisis del Ensamble")
        if btn_predecir and canvas_result.image_data is not None:
            img_array = canvas_result.image_data.astype(np.uint8)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGBA2GRAY)
            resized = cv2.resize(gray, (28,28), interpolation=cv2.INTER_AREA)
            flattened = np.transpose(resized).reshape(1,784)/255.0

            prob_total = None
            resultados = []

            for nombre, modelo_cargado in modelos.items():
                if isinstance(modelo_cargado, tuple):
                    transformador, modelo = modelo_cargado
                    X = transformador.transform(flattened)
                else:
                    modelo = modelo_cargado
                    X = flattened
                if hasattr(modelo, "predict_proba"):
                    prob = modelo.predict_proba(X)[0]
                else:
                    pred = modelo.predict(X)[0]
                    prob = np.zeros(len(EMNIST_MAPPING))
                    prob[pred]=1
                prob_total = prob if prob_total is None else prob_total + prob
                idx = np.argsort(prob)[-3:][::-1]
                top1, top2, top3 = idx
                c1, c2, c3 = prob[top1], prob[top2], prob[top3]
                p1, p2, p3 = EMNIST_MAPPING[top1], EMNIST_MAPPING[top2], EMNIST_MAPPING[top3]
                resultados.append({
                    "Modelo": nombre,
                    "Predicción 1": f"{p1} ({c1*100:.1f}%)",
                    "Predicción 2": f"{p2} ({c2*100:.1f}%)",
                    "Predicción 3": f"{p3} ({c3*100:.1f}%)"
                })
            prob_prom = prob_total / len(modelos)
            final_char = EMNIST_MAPPING[np.argmax(prob_prom)]
            confianza = np.max(prob_prom)
            color = "green" if confianza >= 0.6 else "red"
            st.markdown(f"""
            <div style="background-color:#1E1E1E; border:2px solid {color}; border-radius:12px; padding:20px; text-align:center;">
                <h3 style="color:#9E9E9E; margin:0;">Consenso Final</h3>
                <h1 style="color:white; font-size:60px; margin:0;">{final_char}</h1>
                <p style="color:{color}; font-size:20px; margin:0;">Confianza: {confianza*100:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("**Desglose por Modelo:**")
            st.dataframe(pd.DataFrame(resultados), use_container_width=True, hide_index=True)
        else:
            st.info("Dibuja algo en el lienzo y presiona 'Ejecutar Modelos'.")

# =======================
# TAB MONTE CARLO
# =======================
with tab_montecarlo:
    st.title("Simulación Monte Carlo y Cálculo de VaR")
    st.sidebar.header("Parámetros de la Simulación")
    ticker_symbol = st.sidebar.text_input("Ticker del Activo (ej. SPY, AAPL)", "SPY").upper().strip()
    dias_simulacion = st.sidebar.slider("Días a simular hacia el futuro", 10, 252, 30)
    # Continuación de Monte Carlo
    num_simulaciones = st.sidebar.slider("Número de escenarios", 100, 5000, 1000, step=100)

    if ticker_symbol:
        @st.cache_data
        def get_historical_data(ticker):
            try:
                stock = yf.Ticker(ticker)
                data = stock.history(period="1y")
                return data['Close']
            except Exception:
                return pd.Series(dtype='float64')

        with st.spinner('Descargando historial...'):
            precios = get_historical_data(ticker_symbol)

        if precios.empty:
            st.error(f"No se encontraron datos para '{ticker_symbol}'.")
        else:
            # Cálculos
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
            for t in range(1, dias_simulacion):
                price_paths[t] = price_paths[t-1] * retornos_diarios_simulados[t]

            st.success(f"¡Simulación completada! {num_simulaciones} escenarios para {dias_simulacion} días.")

            # Visualización
            col1, col2 = st.columns([2,1])
            with col1:
                st.subheader(f"Trayectorias Simuladas para {ticker_symbol}")
                lineas_a_graficar = min(200, num_simulaciones)
                fig_paths = go.Figure()
                for i in range(lineas_a_graficar):
                    fig_paths.add_trace(go.Scatter(y=price_paths[:,i], mode='lines',
                                                   line=dict(width=1, color='rgba(0,100,255,0.1)'), showlegend=False))
                fig_paths.add_trace(go.Scatter(x=[0,dias_simulacion], y=[precio_actual, precio_actual],
                                               mode='lines', name='Precio Actual', line=dict(color='red', width=2, dash='dash')))
                fig_paths.update_layout(height=400, template="plotly_white", xaxis_title="Días hacia el futuro",
                                        yaxis_title="Precio Simulado ($)")
                st.plotly_chart(fig_paths, use_container_width=True)
            with col2:
                st.subheader("Análisis de Riesgo")
                precios_finales = price_paths[-1]
                p_95 = np.percentile(precios_finales, 95)
                p_50 = np.percentile(precios_finales, 50)
                p_5 = np.percentile(precios_finales, 5)
                st.metric("Precio Actual", f"${precio_actual:.2f}")
                st.markdown("---")
                st.metric("Mejor Escenario (P95)", f"${p_95:.2f}", delta=f"{((p_95/precio_actual)-1)*100:.2f}%")
                st.metric("Escenario Esperado (Mediana)", f"${p_50:.2f}", delta=f"{((p_50/precio_actual)-1)*100:.2f}%")
                st.metric("Peor Escenario (P5 / VaR)", f"${p_5:.2f}", delta=f"{((p_5/precio_actual)-1)*100:.2f}%")
                st.info("El Percentil 5% representa el 'Value at Risk' (VaR).")

# =======================
# TAB SERIES TEMPORALES
# =======================
with tab_series:
    st.title("Análisis de Series Temporales")
    st.sidebar.header("Parámetros Series Temporales")
    ticker_symbol_ts = st.sidebar.text_input("Ticker (ej. AAPL, SPY)", "AAPL").upper().strip()
    start_date = st.sidebar.date_input("Fecha de inicio", date.today()-timedelta(days=365))
    end_date = st.sidebar.date_input("Fecha de fin", date.today())

    if ticker_symbol_ts and start_date < end_date:
        @st.cache_data
        def load_data(ticker, start, end):
            try:
                start_str = start.strftime('%Y-%m-%d')
                end_str = end.strftime('%Y-%m-%d')
                data = yf.download(ticker, start=start_str, end=end_str, progress=False)
                if not data.empty:
                    data.reset_index(inplace=True)
                    if 'Date' in data.columns:
                        data['Date'] = pd.to_datetime(data['Date']).dt.tz_localize(None)
                return data
            except Exception:
                return pd.DataFrame()

        with st.spinner("Descargando datos financieros..."):
            data = load_data(ticker_symbol_ts, start_date, end_date)

        if data.empty:
            st.error(f"No se encontraron datos para '{ticker_symbol_ts}'")
        else:
            st.success("¡Datos cargados exitosamente!")
            if st.checkbox("Mostrar datos en crudo (Raw Data)"):
                st.write(data.tail())

            # Medias móviles
            data['MA50'] = data['Close'].rolling(50).mean()
            data['MA200'] = data['Close'].rolling(200).mean()

            st.subheader(f"Gráfico de Velas y Medias Móviles para {ticker_symbol_ts}")
            fig = go.Figure()
            fig.add_trace(go.Candlestick(x=data['Date'], open=data['Open'], high=data['High'],
                                         low=data['Low'], close=data['Close'], name='Precio'))
            fig.add_trace(go.Scatter(x=data['Date'], y=data['MA50'], line=dict(color='blue', width=1.5), name='MA50'))
            fig.add_trace(go.Scatter(x=data['Date'], y=data['MA200'], line=dict(color='red', width=1.5), name='MA200'))
            fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Ingresa un ticker válido y asegúrate que la fecha de inicio sea anterior a la fecha de fin.")
