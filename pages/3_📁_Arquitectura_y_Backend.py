import streamlit as st

st.set_page_config(page_title="Proyectos Académicos", layout="wide")

st.title("🎓 Proyectos Académicos: Universidad Politécnica de Victoria")
st.markdown("""
Como estudiante de **Ingeniería en Tecnologías de la Información (ITI)**, he desarrollado proyectos 
enfocados en la comprensión profunda de algoritmos, bases de datos y arquitectura de software. 
Estos trabajos reflejan mi capacidad para trasladar la teoría computacional a código funcional.
""")

st.divider()

# ==========================================
# PROYECTO 1: EDULIBRERIA (C++)
# ==========================================
with st.expander("📚 Edulibreria | Estructuras de Datos Avanzadas en C++", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Objetivo Académico
        Comprender el manejo de memoria y la implementación manual de estructuras de datos complejas sin depender de librerías de alto nivel.
        
        ### Desarrollo Técnico
        * **Implementación:** Desarrollo de un software de gestión de inventario utilizando C++ puro.
        * **Algoritmia:** Programación de árboles y listas enlazadas para la búsqueda, inserción y eliminación eficiente de registros.
        * **Optimización:** Reducción del *overhead* computacional al estructurar los datos de manera lógica, un principio fundamental para el cómputo de alto rendimiento en modelos matemáticos.
        """)
    with col2:
        st.info("**Conceptos Clave:**\n\n* C++\n* Manejo de Memoria\n* Complejidad Algorítmica")
        st.link_button("Ver Código en GitHub", "https://github.com/TU_USUARIO/edulibreria", use_container_width=True)

# ==========================================
# PROYECTO 2: ITICRITICS (SQL)
# ==========================================
with st.expander("🎬 Iticritics | Diseño de Bases de Datos Relacionales (SQL)"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Objetivo Académico
        Diseñar una arquitectura de base de datos normalizada e integrarla con un servidor backend para manejar flujos de información estructurada.
        
        ### Desarrollo Técnico
        * **Modelado de Datos:** Creación de esquemas relacionales robustos (SQL) para gestionar perfiles de usuario, reseñas y metadatos.
        * **Consultas (Queries):** Optimización de peticiones a la base de datos para garantizar baja latencia en la recuperación de información concurrente.
        * **Integración Backend:** Uso de Node.js y JavaScript (ES6+) para construir la lógica del servidor y asegurar la integridad de los datos.
        """)
    with col2:
        st.info("**Conceptos Clave:**\n\n* SQL Normalizado\n* Node.js\n* Arquitectura Cliente-Servidor")
        st.link_button("Ver Código en GitHub", "https://github.com/TU_USUARIO/iticritics", use_container_width=True)

# ==========================================
# PROYECTO 3: FLOODED (NoSQL)
# ==========================================
with st.expander("🌊 Flooded | Desarrollo Full Stack y Bases de Datos NoSQL"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Objetivo Académico
        Aplicar metodologías ágiles en la construcción de una plataforma integral (MERN Stack), enfocándose en la escalabilidad y la flexibilidad de los datos.
        
        ### Desarrollo Técnico
        * **Esquemas Flexibles:** Diseño de la base de datos utilizando MongoDB y Mongoose, ideal para manejar estructuras de datos no estructuradas o en constante cambio.
        * **API RESTful:** Programación de endpoints con Express.js para procesar operaciones CRUD de forma segura y eficiente.
        * **Interfaz de Usuario:** Conexión del backend con un frontend dinámico construido en React.js, demostrando dominio de todo el flujo de vida del dato.
        """)
    with col2:
        st.info("**Conceptos Clave:**\n\n* MongoDB (NoSQL)\n* Creación de APIs\n* React.js")
        st.link_button("Ver Código en GitHub", "https://github.com/TU_USUARIO/flooded", use_container_width=True)

st.divider()
