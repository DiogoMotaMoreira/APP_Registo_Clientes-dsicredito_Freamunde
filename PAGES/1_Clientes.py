import streamlit as st
import mysql.connector as mc
import pandas as pd

bd = mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="sebastianas"
)


cursor = bd.cursor()
cursor.execute("SELECT nome, email, telemovel FROM cliente")
clientes = cursor.fetchall()

df = pd.DataFrame( clientes ,columns=("nome", "email", "telemóvel"))

st.write("## Lista de Clientes")
if clientes:
    st.dataframe(df)
else:
    st.info("Nenhum cliente encontrado.")

    