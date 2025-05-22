from Controllers.ClienteController import get_clientes, add_cliente
import streamlit as st

st.set_page_config(layout="wide")
st.title("Gerenciamento de Clientes")

# --- Seção para Adicionar Cliente ---
st.header("Adicionar Novo Cliente")
with st.form("add_cliente_form"): # Usar um formulário para submissão única
    new_nome = st.text_input("Nome", key="input_nome")
    new_idade = st.text_input("Idade", key="input_idade")
    new_profissao = st.text_input("Profissão", key="input_profissao")

    submitted = st.form_submit_button("Adicionar Cliente")

    if submitted:
        if new_nome and new_idade and new_profissao:
            add_cliente(new_nome, new_idade, new_profissao)
            st.success(f"Cliente '{new_nome}' adicionado!")
            st.session_state['clientes_needs_refresh'] = True
        else:
            st.warning("Por favor, preencha todos os campos: Nome, Idade e Profissão.")

# --- Seção para Lista de Clientes ---
st.write("### Lista de Clientes")

# 1. Inicializa o estado da sessão para armazenar os clientes
#    e um sinalizador para saber quando recarregar
if 'clientes_data' not in st.session_state:
    st.session_state['clientes_data'] = [] # Lista vazia inicialmente
if 'clientes_needs_refresh' not in st.session_state:
    st.session_state['clientes_needs_refresh'] = True # Força a primeira carga

# 2. Botão para forçar a atualização manual da lista
if st.button("Atualizar Lista de Clientes"):
    st.session_state['clientes_needs_refresh'] = True

# 3. Condição para recarregar os clientes APENAS QUANDO NECESSÁRIO
if st.session_state['clientes_needs_refresh']:
    with st.spinner('Carregando clientes...'): # Feedback visual enquanto carrega
        clientes_carregados = get_clientes()
        st.session_state['clientes_data'] = clientes_carregados
    st.session_state['clientes_needs_refresh'] = False # Reseta o sinalizador

# 4. Exibe os clientes que estão armazenados no estado da sessão
if st.session_state['clientes_data']:
    # st.table é bom para exibição tabular de todos os dados
    st.table(st.session_state['clientes_data'])

    # Ou, se preferir uma exibição personalizada como antes:
    # for cliente in st.session_state['clientes_data']:
    #     # Certifique-se de que as chaves 'nome' e 'profissao' existem nos dados retornados
    #     # O print(clientes) que você tinha antes ajudou a ver a estrutura
    #     st.write(f"- {cliente['nome']} ({cliente['profissao']})")
else:
    st.info("Nenhum cliente encontrado. Adicione um acima ou clique em 'Atualizar Lista de Clientes'.")

# O print(clientes) que você tinha, se for apenas para depuração,
# pode ser removido ou movido para dentro do bloco `if st.session_state['clientes_needs_refresh']:`
# para que só apareça quando a chamada real ao DB acontecer.