import streamlit as st
import numpy as np
import cv2
import joblib
import os
import pandas as pd
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Clasificador EMNIST", layout="wide")

st.title("🧠 Reconocimiento Óptico: Clasificador EMNIST")
st.markdown("""
Esta aplicación utiliza **Visión por Computadora (OpenCV)** y un ensamble de modelos de **Machine Learning (Scikit-Learn)** para reconocer caracteres escritos a mano en tiempo real.
""")

EMNIST_MAPPING = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt"

# ==========================================
# CARGA DE MODELOS (Caché para no recargar en cada trazo)
# ==========================================
@st.cache_resource
def cargar_modelos():
    modelos = {}
    carpeta = "clasificadores"
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            if archivo.endswith(".pkl"):
                ruta = os.path.join(carpeta, archivo)
                nombre = archivo.replace(".pkl", "")
                try:
                    modelos[nombre] = joblib.load(ruta)
                except Exception as e:
                    st.error(f"Error al cargar {nombre}: {e}")
    return modelos

modelos = cargar_modelos()

# ==========================================
# INTERFAZ GRÁFICA (LIENZO Y RESULTADOS)
# ==========================================
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Lienzo de Dibujo")
    st.info("Dibuja un número o letra en el recuadro negro:")
    
    # Reemplazo de PyQt6 por st_canvas
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
            st.warning("⚠️ No se encontraron modelos (.pkl) en la carpeta 'clasificadores'.")
        else:
            with st.spinner("Procesando imagen e inferencias..."):
                # 1. Procesamiento de la imagen (idéntico a tu lógica original)
                img_array = canvas_result.image_data.astype(np.uint8) # Formato RGBA
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGBA2GRAY) # Convertir a escala de grises
                resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
                transposed = np.transpose(resized)
                flattened = transposed.reshape(1, 784) / 255.0

                # 2. Ejecución de modelos
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

                    # Acumular probabilidad para el consenso
                    if prob_total is None:
                        prob_total = prob.copy()
                    else:
                        prob_total += prob

                    # Top 3 de este modelo
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

                # 3. Consenso Final
                prob_prom = prob_total / len(modelos)
                final_idx = np.argmax(prob_prom)
                final_char = EMNIST_MAPPING[final_idx]
                confianza = np.max(prob_prom)

                # Tarjeta de Consenso (Recreando el estilo de tu cuadro de PyQt6)
                color = "green" if confianza >= 0.6 else "red"
                st.markdown(f"""
                <div style="background-color:#1E1E1E; border:2px solid {color}; border-radius:12px; padding:20px; text-align:center;">
                    <h3 style="color:#9E9E9E; margin:0;">Consenso Final</h3>
                    <h1 style="color:white; font-size:60px; margin:0;">{final_char}</h1>
                    <p style="color:{color}; font-size:20px; margin:0;">Confianza: {confianza*100:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("") # Espacio
                
                # Tabla de resultados individuales
                st.markdown("**Desglose por Modelo:**")
                df_resultados = pd.DataFrame(resultados)
                st.dataframe(df_resultados, use_container_width=True, hide_index=True)
    else:
        st.info("👈 Dibuja algo en el lienzo y presiona 'Ejecutar Modelos' para ver el desglose matemático.")
