# 🚀 DSIcréditos Freamunde: Sistema de Registo de Clientes

<!-- Adicione aqui um banner ou logo do projeto, se houver. Ex: ![Banner do Projeto](link_para_sua_imagem.png) -->

## 📝 Descrição Curta

Esta aplicação web, desenvolvida em **Python** com **Streamlit**, oferece uma solução simples e eficaz para o registo e gestão de clientes para eventos da DSIcréditos Freamunde. Ela permite adicionar, visualizar e remover registos de clientes de forma intuitiva, armazenando os dados de forma persistente em **ficheiros de texto**.

## 🎬 Demonstração

Para uma visão rápida das funcionalidades, confira:

*   **GIF/Vídeo de Demonstração:** ![Demonstração](./assets/v.gif)

## � Tecnologias

Este projeto utiliza as seguintes tecnologias:

*   **Python**: Linguagem de programação principal.
    ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
*   **Streamlit**: Framework para construção rápida de aplicações web interativas.
    ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
*   **Pandas**: Biblioteca para manipulação e análise de dados (usada para exibir a lista de clientes).
    !Pandas

## 📦 Instalação

Para configurar e rodar o projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    (Você precisará criar um arquivo `requirements.txt` com `streamlit`, `pandas`)

4.  **Ficheiro de Dados:**
    *   A aplicação irá criar automaticamente um ficheiro chamado `clientes.txt` no diretório raiz do projeto para armazenar os dados dos clientes. Não é necessária nenhuma configuração manual.

## ▶️ Como usar

Após a instalação e configuração do banco de dados, inicie a aplicação Streamlit:
```bash
streamlit run Registo.py
```
Interaja com a interface para cadastrar clientes no evento.

## 🗄️ Banco de Dados
A aplicação utiliza MariaDB para armazenar os registros. O script de inicialização do banco está incluído no diretório principal.
