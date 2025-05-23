# meu_projeto_streamlit/main.py (ou crud/main.py)
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="Meu App CRUD",
    page_icon="👋",
)

st.write("# Bem-vindo ao Meu App CRUD! 👋")

st.sidebar.success("Selecione uma página acima.")

st.markdown(
    """
    Este é um aplicativo CRUD básico construído com Streamlit e Supabase.
    """
)