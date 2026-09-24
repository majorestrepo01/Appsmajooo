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
    
    /* Estilo de Tarjeta para cada aplicación */
    .app-card {
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 18px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .app-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }
    .date-badge {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.95rem;
        display: inline-block;
        margin-bottom: 15px;
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
    
    st.markdown("---")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown(f"🔗 **Sitio Oficial:** [Páginas y ejercicios]({url_ia})")

# 4. Encabezado Principal con Marco Degradado
st.markdown("""
    <div class="header-frame">
        <h1 style="margin:0; font-size: 2.3rem;">Mis Aplicaciones de Inteligencia Artificial 🤖✨</h1>
        <p style="margin-top: 8px; color: #6b7280; font-size: 1.05rem;">
            Repositorio con todos los proyectos e interfaces desarrolladas organizados por fecha.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 5. Organización en Columnas por Fecha
col1, col2, col3, col4 = st.columns(4, gap="medium")

# --- COLUMNA 1: 20 DE AGOSTO ---
with col1:
    st.markdown('<div class="date-badge">📅 20 de Agosto</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>📱 Mi Primera App</h3>
            <p>Primera aplicación interactiva desarrollada en Streamlit.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://miprimeraappmajo.streamlit.app/", use_container_width=True)
    
    st.write("") # Espaciador
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>🔊 Texto a Audio</h3>
            <p>Conversión de texto escrito a síntesis de voz mediante IA.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://repositorioprofeinterfaces.streamlit.app/", use_container_width=True)

# --- COLUMNA 2: 27 DE AGOSTO ---
with col2:
    st.markdown('<div class="date-badge">📅 27 de Agosto</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>🌐 Traductor</h3>
            <p>Herramienta para traducción automática de textos en tiempo real.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://ocr-audio-major.streamlit.app/", use_container_width=True)
        
    st.write("")
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>📄 OCR Tradicional</h3>
            <p>Extracción automática de texto legible desde imágenes.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://ocr-normal-major.streamlit.app/", use_container_width=True)
        
    st.write("")
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>🎙️ OCR + Audio</h3>
            <p>Extracción de texto desde imágenes y lectura automática en voz alta.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://ocr-audio-major.streamlit.app/", use_container_width=True)

# --- COLUMNA 3: 3 DE SEPTIEMBRE ---
with col3:
    st.markdown('<div class="date-badge">📅 3 de Septiembre</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>☁️ Wordcloud Studio</h3>
            <p>Generación y visualización interactiva de nubes de palabras.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://wordcloud-majooooo.streamlit.app/", use_container_width=True)
        
    st.write("")
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>🎭 Análisis de Sentimientos</h3>
            <p>Evaluación del tono emocional e intención en textos.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://sentimenta-majooooo.streamlit.app/", use_container_width=True)
        
    st.write("")
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>📊 TF - IDF en Español</h3>
            <p>Procesamiento de Lenguaje Natural para frecuencia de palabras claves.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://tdfff-majo.streamlit.app/", use_container_width=True)

# --- COLUMNA 4: 17 DE SEPTIEMBRE ---
with col4:
    st.markdown('<div class="date-badge">📅 17 de Septiembre</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>🎯 Detección con YOLO</h3>
            <p>Reconocimiento y ubicación de múltiples objetos en imágenes.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://yolovmajoo.streamlit.app", use_container_width=True)
        
    st.write("")
    
    with st.container():
        st.markdown("""
        <div class="app-card">
            <h3>🤖 Teachable Machine</h3>
            <p>Reconocimiento y clasificación de gestos mediante modelos personalizados.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir App 🚀", "https://gestosmajoo.streamlit.app", use_container_width=True)


