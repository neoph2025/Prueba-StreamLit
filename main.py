import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

st.title("Mi app con OpenAI y Streamlit")

api_key_usuario = st.text_input("Introduce tu API_Key", type="password")

if api_key_usuario:

   pregunta_1 = st.text_input('Que desea preguntar ? ... ')

   if st.button("Enviar"):
       chatbot = ChatOpenAI(model="gpt-3.5-turbo-0125",api_key=api_key_usuario)

       messagesToTheChatbot = [
       HumanMessage(content=pregunta_1),
   ]
   respuesta = chatbot.invoke(messagesToTheChatbot)
   st.write(respuesta.content)

