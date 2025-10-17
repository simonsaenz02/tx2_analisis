import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# ----------------- CONFIGURACIÓN -----------------
st.set_page_config(
    page_title="🪞 Espejo Emocional",
    layout="wide",
    page_icon="✨"
)

translator = Translator()

# ----------------- ESTILOS -----------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #f7f8fa, #e9eff1);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #7f8c8d;
        margin-top: 0px;
        margin-bottom: 30px;
    }
    .stButton>button {
        background: linear-gradient(to right, #16a085, #27ae60);
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(to right, #27ae60, #16a085);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- ENCABEZADO -----------------
st.markdown("<p class='title'>🪞 Espejo Emocional</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Escribe tus pensamientos y descubre la emoción oculta en tus palabras ✨</p>", unsafe_allow_html=True)


# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.header("📖 Guía de interpretación")
    st.markdown(
        """
        **Polaridad** 🌓  
        - Va de **-1** (muy negativo) a **1** (muy positivo).  
        - **0** indica neutralidad.  

        **Subjetividad** 🎭  
        - Va de **0** (muy objetivo, hechos) a **1** (muy subjetivo, opiniones).  
        - Un texto subjetivo refleja emociones, creencias y opiniones.  
        """
    )
    st.info("💡 Tip: Escribe frases espontáneas para ver cómo cambian tus emociones en el análisis.")


# ----------------- EXPANDER 1 -----------------
with st.expander('🔍 Analizar Polaridad y Subjetividad'):
    text1 = st.text_area('✏️ Escribe tu frase aquí:')
    if text1:
        # Traducción al inglés antes de usar TextBlob
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        # Resultados
        st.write('**Polaridad:** ', round(blob.sentiment.polarity, 2))
        st.write('**Subjetividad:** ', round(blob.sentiment.subjectivity, 2))

        # Interpretación
        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.success('🌞 Tu mensaje refleja un sentimiento **Positivo**')
        elif x <= -0.5:
            st.error('🌧️ Tu mensaje refleja un sentimiento **Negativo**')
        else:
            st.info('🌗 Tu mensaje refleja un sentimiento **Neutral**')


# ----------------- EXPANDER 2 -----------------
with st.expander('📝 Corrección de texto en inglés'):
    text2 = st.text_area('✏️ Escribe un texto en inglés para corregir:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.markdown("✨ Versión corregida:")
        st.success(blob2.correct())

