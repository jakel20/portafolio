import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# ------------------------------------------------------------
# Aplicaciones (en orden de sesión)
# ------------------------------------------------------------
apps = [
  {
    "titulo": "Descenso de Gradiente",
    "imagen": "sesion3.png",
    "descripcion": "Explora cómo la tasa de aprendizaje y el punto inicial afectan la convergencia "
                   "del descenso de gradiente hacia el mínimo de una función.",
    "url": "https://sesion-3.streamlit.app/",
  },
  {
    "titulo": "Detector de Anomalías",
    "imagen": "sesion4.png",
    "descripcion": "Simula una alarma con reglas lógicas y compara el rendimiento de soluciones "
                   "ingenuas vs. vectorizadas con notación Big-O y NumPy.",
    "url": "https://sesion4-ll5js9p6xhsf44tv4b44un.streamlit.app/",
  },
  {
    "titulo": "Preparación de Datos",
    "imagen": "sesion5.png",
    "descripcion": "Explora tipos de datos, valores faltantes, outliers, normalización y particiones "
                   "train/val/test con un dataset de sensores IoT.",
    "url": "https://sesion-5-n8dahvwtoacbs5p2twaqbs.streamlit.app/",
  },
  {
    "titulo": "Monitoreo Hidrológico",
    "imagen": "sesion6.png",
    "descripcion": "Consulta el nivel de quebradas de la red MARCO de CORNARE, con umbrales de alerta, "
                   "tendencias, calidad del dato y ubicación de cada estación.",
    "url": "https://sesion6-wsuhhfsi6qiatxft4yotwt.streamlit.app/",
  },
  {
    "titulo": "Regresión",
    "imagen": "sesion7.png",
    "descripcion": "Aprende cómo funciona una regresión lineal: ajuste simple y múltiple, función de costo, "
                   "descenso de gradiente y métricas, con datos reales de vivienda.",
    "url": "https://sesion7-bh4kurgpmjkacyebjzefbl.streamlit.app/",
  },
  {
    "titulo": "Series de Tiempo",
    "imagen": "sesion8.png",
    "descripcion": "Descompone una serie de sensor IoT en tendencia, estacionalidad y ruido, y compara "
                   "modelos de pronóstico: media móvil, Holt-Winters, ARIMA y SARIMA.",
    "url": "https://sesion-8-cau2gzff3we5fbtggqjpar.streamlit.app/",
  },
  {
    "titulo": "Calidad del Aire",
    "imagen": "sesion9.png",
    "descripcion": "Carga tus modelos entrenados (.pkl) y genera pronósticos de PM2.5 y PM10 con datos "
                   "de la red MARCO de CORNARE.",
    "url": "https://sesion9-u2q29okkpcjp6wihcmsajo.streamlit.app/",
  },
  {
    "titulo": "Regresión Logística",
    "imagen": "sesion11.png",
    "descripcion": "Predice si lloverá mañana con regresión logística: elige variables, ajusta el umbral "
                   "de clasificación y observa la curva sigmoide y la importancia de cada variable.",
    "url": "https://sesion11.streamlit.app/",
  },
  {
    "titulo": "Programación Orientada a Objetos",
    "imagen": "sesion15.png",
    "descripcion": "Carga un objeto FlujoModelo (Estandarizador + RegresionLineal), explora sus atributos "
                   "y métodos, y prueba paso a paso cómo predice el consumo energético.",
    "url": "https://sesion-15.streamlit.app/",
  },
  {
    "titulo": "NumPy con Sensores",
    "imagen": "sesion15-2.png",
    "descripcion": "Compara el rendimiento de un ciclo for frente a NumPy y aplica funciones "
                   "vectorizadas (media, máximo, desviación, filtros) sobre lecturas de sensores.",
    "url": "https://sesi-n-15.streamlit.app/",
  },
  {
    "titulo": "Estimador de Vivienda (API)",
    "imagen": "sesion16.png",
    "descripcion": "Estima el valor de una vivienda en California con una regresión lineal entrenada "
                   "por descenso de gradiente, desplegada como API con documentación en /docs.",
    "url": "https://sesion-16.vercel.app/",
  },
  {
    "titulo": "Predicción de Lluvia (API)",
    "imagen": "sesion16-2.png",
    "descripcion": "Calcula la probabilidad de lluvia para mañana a partir de temperatura, humedad y "
                   "viento con regresión logística, desplegada como API con métricas de evaluación.",
    "url": "https://sesion-16-2.vercel.app/",
  },
]

# ------------------------------------------------------------
# Tarjetas en filas de 3 columnas
# ------------------------------------------------------------
for i in range(0, len(apps), 3):
  cols = st.columns(3)
  for col, app in zip(cols, apps[i:i + 3]):
    with col:
      st.subheader(app["titulo"])
      try:
        image = Image.open(app["imagen"])
        st.image(image)
      except FileNotFoundError:
        st.warning(f"No se encontró la imagen '{app['imagen']}'.")
      st.write(app["descripcion"])
      st.write(f"{app['titulo']}: [Enlace]({app['url']})")
