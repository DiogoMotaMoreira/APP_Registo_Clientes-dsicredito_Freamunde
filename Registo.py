import streamlit as st

st.set_page_config(page_title="Registo de Clientes")
st.markdown("## Registo de Clientes")

CLIENT_FILE = "clientes.txt"

with st.form("registo_cliente_form", clear_on_submit=True):

    if "nome_form" not in st.session_state:
        st.session_state.nome_form = ""
    if "email_form" not in st.session_state:
        st.session_state.email_form = ""
    if "num_form" not in st.session_state:
        st.session_state.num_form = ""

    nome = st.text_input(placeholder="Nome Completo", label="Nome Cliente:", key="nome_form")
    email = st.text_input(placeholder="nome@email.com", label="Email Cliente:", key="email_form")
    num = st.text_input(placeholder="telemovel", label="Numero Cliente:", key="num_form")

    enviado = st.form_submit_button("Submeter")

    if enviado:
        if not nome or not email or not num:
            st.warning("Por favor, preencha todos os campos.")
        else:
            client_data = f"{nome},{email},{num}"
            try:
                with open(CLIENT_FILE, "a", encoding="utf-8") as f:
                    f.write(client_data + "\n")
                st.success("Cliente registado com sucesso!")
                
     

            except IOError as e:
                st.error(f"Ocorreu um erro ao registar o cliente: {e}")
