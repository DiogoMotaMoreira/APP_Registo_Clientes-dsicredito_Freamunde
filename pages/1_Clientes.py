import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Lista de Clientes")
st.write("## Lista de Clientes")

CLIENT_FILE = "clientes.txt"

def load_clients_from_file():
    """Carrega os clientes do ficheiro de texto."""
    clientes_data = []
    try:
        if os.path.exists(CLIENT_FILE):
            with open(CLIENT_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            nome, email, telemovel = line.split(',')
                            clientes_data.append({"nome": nome, "email": email, "telemóvel": telemovel})
                        except ValueError:
                            st.warning(f"Linha inválida no ficheiro de clientes: {line}")
    except IOError as e:
        st.error(f"Erro ao ler o ficheiro de clientes: {e}")
    return clientes_data

clientes = load_clients_from_file()

if clientes:
    df = pd.DataFrame(clientes)
    st.dataframe(df)
else:
    st.info("Nenhum cliente encontrado.")