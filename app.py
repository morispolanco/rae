import streamlit as st
import requests
import json

# Configuración de la página
st.set_page_config(page_title="Asistente de Lengua Española", page_icon="🇪🇸")

# Título de la aplicación
st.title("Asistente de Lengua Española")

# Obtener la API key de los secrets de Streamlit
api_key = st.secrets["api_key"]

# Función para hacer la solicitud a la API
def consultar_api(pregunta):
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": f"sk-tune-{api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": "Eres un académico de la lengua española que resuelve dudas y dificultades sobre esta lengua en forma exhaustiva y amable."
            },
            {
                "role": "user",
                "content": pregunta
            }
        ],
        "model": "meta/llama-3.1-405b-instruct",
        "stream": False,
        "frequency_penalty": 0.3,
        "max_tokens": 9000
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error en la solicitud: {response.status_code}"

# Área de entrada de texto para la pregunta del usuario
pregunta_usuario = st.text_area("Escribe tu duda o pregunta sobre el idioma español:", height=100)

# Botón para enviar la pregunta
if st.button("Consultar"):
    if pregunta_usuario:
        with st.spinner("Consultando al académico..."):
            respuesta = consultar_api(pregunta_usuario)
        st.subheader("Respuesta del Académico:")
        st.write(respuesta)
    else:
        st.warning("Por favor, escribe una pregunta antes de consultar.")

# Información adicional
st.sidebar.header("Acerca de esta aplicación")
st.sidebar.write("""
Esta aplicación utiliza un modelo de lenguaje avanzado para responder preguntas y resolver dudas sobre el idioma español. 
El asistente actúa como un académico de la lengua española, proporcionando respuestas exhaustivas y amables.

Puedes preguntar sobre:
- Gramática
- Ortografía
- Vocabulario
- Usos regionales
- Etimología
- Y mucho más...

¡No dudes en hacer cualquier pregunta relacionada con el español!
""")

# Pie de página
st.sidebar.markdown("---")
st.sidebar.markdown("Desarrollado con ❤️ para amantes del español")
