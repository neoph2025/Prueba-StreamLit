import streamlit as st
import openai

st.title("Mi app con OpenAI y Streamlit")

# Recoger la API key ingresada por el usuario
api_key = st.text_input("Introduce tu OpenAI API Key", type="password")

if api_key:
   # Configurar la clave en OpenAI
   openai.api_key = api_key

   prompt = st.text_input("Introduce tu pregunta o texto para consultar")

   if st.button("Enviar"):
       if prompt:
           try:
               response = openai.ChatCompletion.create(
                   model="gpt-3.5-turbo",
                   messages=[
                       {"role": "user", "content": prompt}
                   ]
               )
               respuesta = response.choices[0].message['content']
               st.write(respuesta)
           except Exception as e:
               st.error(f"Error al conectar con OpenAI: {e}")
       else:
           st.warning("Por favor ingresa un texto para consultar")
else:
   st.info("Introduce tu API Key para continuar")