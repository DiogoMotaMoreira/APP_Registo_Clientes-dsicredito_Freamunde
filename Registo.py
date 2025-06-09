import streamlit as st
import mysql.connector as mc

bd = mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="sebastianas"
)


cursor = bd.cursor()


st.markdown("## Registo de Clientes")
nome = st.text_input(placeholder="Nome Completo", label="Nome Cliente:")
email = st.text_input(placeholder="nome@email.com", label="Email Cliente:")
num = st.text_input(placeholder="telemovel", label="Numero Cliente:")

enviado = st.button("Submeter")

if(enviado):
    try:
        cursor.execute("INSERT INTO cliente(nome, email, telemovel) VALUES (%s, %s, %s)", (nome, email, num))
        bd.commit()
        st.success("Cliente registado com sucesso!")
    except Exception:
        st.error(f"Ocorreu um erro ao registar o cliente.")
