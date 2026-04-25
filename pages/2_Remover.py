import streamlit as st
import os

st.set_page_config(page_title="Remover Cliente")
st.markdown("## Remover Cliente")

CLIENT_FILE = "clientes.txt"

def load_clients():
    clients = []
    try:
        if os.path.exists(CLIENT_FILE):
            with open(CLIENT_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    clients.append(line.strip())
    except IOError as e:
        st.error(f"Erro ao ler o ficheiro de clientes: {e}")
    return clients

nome = st.text_input(placeholder="Nome Completo", label="Nome Cliente:")
bnome = st.button("Eliminar por nome")
email = st.text_input(placeholder="nome@email.com", label="Email Cliente:")
bemail = st.button("Eliminar por email")
num = st.text_input(placeholder="telemovel", label="Numero Cliente:")
btelemovel = st.button("Eliminar por telemovel")

def save_clients(clients_list):
    try:
        with open(CLIENT_FILE, "w", encoding="utf-8") as f:
            for client_line in clients_list:
                f.write(client_line + "\n")
    except IOError as e:
        st.error(f"Erro ao escrever no ficheiro de clientes: {e}")

if bnome or bemail or btelemovel:
    current_clients = load_clients()
    updated_clients = []
    removed_count = 0

    for client_line in current_clients:
        parts = client_line.split(',')
        if len(parts) == 3:
            client_nome, client_email, client_telemovel = parts
            should_remove = False
            if bnome and nome and client_nome == nome:
                should_remove = True
            if bemail and email and client_email == email:
                should_remove = True
            if btelemovel and num and client_telemovel == num:
                should_remove = True

            if not should_remove:
                updated_clients.append(client_line)
            else:
                removed_count += 1
        else:
            updated_clients.append(client_line) # Manter linhas mal formatadas, ou decidir o que fazer com elas

    if bnome and not nome:
        st.warning("Por favor, insira um nome para eliminar.")
    elif bemail and not email:
        st.warning("Por favor, insira um email para eliminar.")
    elif btelemovel and not num:
        st.warning("Por favor, insira um número de telemóvel para eliminar.")
    elif removed_count > 0:
        save_clients(updated_clients)
        st.success(f"{removed_count} cliente(s) eliminado(s) com sucesso!")
    else:
        st.info("Nenhum cliente correspondente foi encontrado para eliminação.")