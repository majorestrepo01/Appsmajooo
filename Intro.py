import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Repositorio de Aplicaciones IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos CSS Personalizados
st.markdown("""
    <style>
    /* Estilo del encabezado principal con degradado */
    .header-frame {
        position: relative;
        padding: 25px;
        border-radius: 16px;
        background: #ffffff;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        border: 3px solid transparent;
        background-clip: padding-box;
    }
    .header-frame::before {
        content: '';
        position: absolute;
        top: -3px; right: -3px; bottom: -3px; left: -3px;
        z-index: -1;
        border-radius: 18px;
        background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
    }
    @media (prefers-color-scheme: dark) {
        .header-frame {
            background: #0e1117;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        }
    }
    
    /* Estilo de Tarjeta adaptable (sin altura fija para evitar cortes de texto) */
    .app-card {
        background-color: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(128, 128, 128, 0.25);
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 12px;
        min-height: 120px;
    }
    .app-card h3 {
        margin: 0 0 8px 0;
        font-size: 1.15rem;
    }
    .app-card p {
        margin: 0;
        font-size: 0.92rem;
        line-height: 1.4;
        color: #6b7280;
    }
    @media (prefers-color-scheme: dark) {
        .app-card p {
            color: #9ca3af;
        }
    }

    /* Etiqueta de fecha para la fila */
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Estilo personalizado para los botones de abrir app */
    .stLinkButton > a {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stLinkButton > a:hover {
        background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 15px rgba(99, 102, 241, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Barra Lateral (Sidebar)
with st.sidebar:
    st.title("📚 Repositorio de IA")
    st.caption("Portafolio de Proyectos")
    
    st.markdown("---")
    st.markdown(
        "La **Inteligencia Artificial** permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )

# 4. Encabezado Principal con Marco Degradado
st.markdown("""
    <div class="header-frame">
        <h1 style="margin:0; font-size: 2.3rem;">Mis Aplicaciones de Inteligencia Artificial ✨</h1>
        <p style="margin-top: 8px; color: #6b7280; font-size: 1.05rem;">
            Repositorio interactivo de proyectos e interfaces organizadas cronológicamente por fecha de clase.
        </p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# FILA 1: 20 DE AGOSTO
# ==========================================
st.markdown('<div class="section-title">📅 Clase: 20 de Agosto</div>', unsafe_allow_html=True)
col1, col2, _ = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown("""
    <div class="app-card">
        <h3>📱 Mi Primera App</h3>
        <p>Primera aplicación interactiva desarrollada en Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://miprimeraappmajo.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
    <div class="app-card">
        <h3>🔊 Texto a Audio</h3>
        <p>Conversión de texto escrito a síntesis de voz mediante IA.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://repositorioprofeinterfaces.streamlit.app/", use_container_width=True)

st.markdown("---")

# ==========================================
# FILA 2: 27 DE AGOSTO
# ==========================================
st.markdown('<div class="section-title">📅 Clase: 27 de Agosto</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown("""
    <div class="app-card">
        <h3>🌐 Traductor</h3>
        <p>Herramienta para traducción automática de textos en tiempo real.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://ocr-audio-major.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
    <div class="app-card">
        <h3>📄 OCR Tradicional</h3>
        <p>Extracción automática de texto legible desde imágenes.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://ocr-normal-major.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("""
    <div class="app-card">
        <h3>🎙️ OCR + Audio</h3>
        <p>Extracción de texto desde imágenes y lectura automática en voz alta.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://ocr-audio-major.streamlit.app/", use_container_width=True)

st.markdown("---")

# ==========================================
# FILA 3: 3 DE SEPTIEMBRE
# ==========================================
st.markdown('<div class="section-title">📅 Clase: 3 de Septiembre</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown("""
    <div class="app-card">
        <h3>☁️ Wordcloud Studio</h3>
        <p>Generación y visualización interactiva de nubes de palabras.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://wordcloud-majooooo.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
    <div class="app-card">
        <h3>🎭 Análisis de Sentimientos</h3>
        <p>Evaluación del tono emocional e intención en textos.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://sentimenta-majooooo.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("""
    <div class="app-card">
        <h3>📊 TF - IDF en Español</h3>
        <p>Procesamiento de Lenguaje Natural para frecuencia de palabras claves.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://tdfff-majo.streamlit.app/", use_container_width=True)

st.markdown("---")

# ==========================================
# FILA 4: 17 DE SEPTIEMBRE
# ==========================================
st.markdown('<div class="section-title">📅 Clase: 17 de Septiembre</div>', unsafe_allow_html=True)
col1, col2, _ = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown("""
    <div class="app-card">
        <h3>🎯 Detección con YOLO</h3>
        <p>Reconocimiento y ubicación de múltiples objetos en imágenes.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://yolovmajoo.streamlit.app", use_container_width=True)

with col2:
    st.markdown("""
    <div class="app-card">
        <h3>🤖 Teachable Machine</h3>
        <p>Reconocimiento y clasificación de gestos mediante modelos personalizados.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir App 🚀", "https://gestosmajoo.streamlit.app", use_container_width=True)
