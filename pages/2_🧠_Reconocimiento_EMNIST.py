import streamlit as st
import numpy as np
import cv2
import joblib
import os
import pandas as pd
import gdown  
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Clasificación EMNIST", layout="wide")

st.title("Reconocimiento Óptico: Modelo de Clasificación EMNIST")
st.markdown("""
**Caso de Estudio: Implementación de Algoritmos de Machine Learning**

Integración de técnicas de Visión por Computadora (OpenCV) y el despliegue de un ensamble de modelos predictivos (Scikit-Learn). El sistema procesa matrices de imágenes en tiempo real, normaliza los datos y ejecuta inferencias estadísticas para clasificación.
""")

st.warning("""
**Nota Técnica de Arquitectura:** Como requerimiento estricto de este proyecto académico, la extracción de características y el entrenamiento del modelo se limitaron exclusivamente a un subconjunto pre-generado de la base de datos *EMNIST Balanced*. 

Por lo tanto, la generalización del modelo ante trazos que se desvían de esa distribución específica presenta una eficiencia reducida. El objetivo principal de este desarrollo es demostrar la arquitectura de integración del ensamble algorítmico y el procesamiento de datos por lotes, priorizando la estructura del pipeline de datos sobre la precisión predictiva absoluta bajo estos parámetros restringidos.
""")

EMNIST_MAPPING = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt"

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
            with st.spinner(f"Descargando {nombre} desde Drive (esto solo pasa la primera vez)..."):
                gdown.download(id=file_id, output=ruta_local, quiet=False)
        try:
            modelos[nombre] = joblib.load(ruta_local)
        except Exception as e:
            st.error(f"Error al cargar {nombre}: {e}")
            
    return modelos

modelos = cargar_modelos()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Lienzo de Dibujo")
    st.info("Dibuja un número o letra en el recuadro negro:")
    
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
        if not modelos:
            st.warning("Hubo un problema cargando los modelos.")
        else:
            with st.spinner("Procesando imagen e inferencias..."):
                img_array = canvas_result.image_data.astype(np.uint8)
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGBA2GRAY)
                resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
                transposed = np.transpose(resized)
                flattened = transposed.reshape(1, 784) / 255.0

                prob_total = None
                resultados = []

                for nombre, modelo_cargado in modelos.items():
                    X = flattened
                    
                    if isinstance(modelo_cargado, tuple):
                        transformador, modelo = modelo_cargado
                        if hasattr(transformador, "transform"):
                            X = transformador.transform(flattened)
                    else:
                        modelo = modelo_cargado

                    if hasattr(modelo, "predict_proba"):
                        prob = modelo.predict_proba(X)[0]
                    else:
                        pred = modelo.predict(X)[0]
                        prob = np.zeros(len(EMNIST_MAPPING))
                        prob[pred] = 1.0

                    if prob_total is None:
                        prob_total = prob.copy()
                    else:
                        prob_total += prob

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
                final_idx = np.argmax(prob_prom)
                final_char = EMNIST_MAPPING[final_idx]
                confianza = np.max(prob_prom)

                color = "green" if confianza >= 0.6 else "red"
                st.markdown(f"""
                <div style="background-color:#1E1E1E; border:2px solid {color}; border-radius:12px; padding:20px; text-align:center;">
                    <h3 style="color:#9E9E9E; margin:0;">Consenso Final</h3>
                    <h1 style="color:white; font-size:60px; margin:0;">{final_char}</h1>
                    <p style="color:{color}; font-size:20px; margin:0;">Confianza: {confianza*100:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("")
                
                st.markdown("**Desglose por Modelo:**")
                df_resultados = pd.DataFrame(resultados)
                st.dataframe(df_resultados, use_container_width=True, hide_index=True)
    else:
        st.info("Dibuja algo en el lienzo y presiona 'Ejecutar Modelos'.")