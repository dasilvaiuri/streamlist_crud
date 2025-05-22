from Controllers.ClienteController import get_clientes, add_cliente
import streamlit as st

st.title("Gerenciamento de Clientes")

nome = st.text_input("Nome")
idade = st.text_input("Idade")
profissao = st.text_input("Profissão")

if st.button("Adicionar Cliente"):
    if nome and idade and profissao:
        add_cliente(nome, idade, profissao)
        st.success(f"Cliente '{nome}' adicionado!")

st.write("### Lista de Clientes")
clientes = get_clientes()
print(clientes)  # Veja a estrutura dos dados retornados
for cliente in clientes:
    st.write(f"- {cliente['nome']} ({cliente['profissao']})")
    #st.write(f"- {cliente.nome} ({cliente.profissao})")