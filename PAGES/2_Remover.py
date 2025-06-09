import streamlit as st
import mysql.connector as mc

bd = mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="sebastianas"
)

cursor = bd.cursor()

st.markdown("## Remover Cliente")

nome = st.text_input(placeholder="Nome Completo", label="Nome Cliente:")
bnome = st.button("Eliminar por nome")
email = st.text_input(placeholder="nome@email.com", label="Email Cliente:")
bemail = st.button("Eliminar por email")
num = st.text_input(placeholder="telemovel", label="Numero Cliente:")
btelemovel = st.button("Eliminar por telemovel")



if(bnome):
    try:
        cursor.execute("DELETE FROM cliente WHERE nome= \""+nome+"\";")
        bd.commit()
        st.success("Cliente eliminado com sucesso!")
    except Exception:
        st.error(f"Ocorreu um erro ao eliminar o cliente.")

if(bemail):
    try:
        cursor.execute("DELETE FROM cliente WHERE email=\""+email+"\";")
        bd.commit()
        st.success("Cliente eliminado com sucesso!")
    except Exception:
        st.error(f"Ocorreu um erro ao eliminar o cliente.")

if(btelemovel):
    try:
        cursor.execute("DELETE FROM cliente WHERE telemovel=\""+num+"\";")
        bd.commit()
        st.success("Cliente eliminado com sucesso!")
    except Exception:
        st.error(f"Ocorreu um erro ao eliminar o cliente.")