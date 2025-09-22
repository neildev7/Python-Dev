# streamlit - frontend e backend
import streamlit as st
from openai import OpenAI

# Inicializa o modelo da OpenAI com uma chave API
modelo = OpenAI(api_key="Digite sua chave API aqui")

# Escreve um título no aplicativo usando markdown
st.write("### ChatBot com IA") # markdown

# session_state = memoria do streamlit
# Verifica se a lista de mensagens já existe no estado da sessão, caso contrário, inicializa uma lista vazia
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# Exibe o histórico de mensagens armazenadas no estado da sessão
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]  # Define o papel da mensagem (usuário ou assistente)
    content = mensagem["content"]  # Conteúdo da mensagem
    st.chat_message(role).write(content)  # Exibe a mensagem no chat

# Captura a entrada do usuário no chat
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    # Exibe a mensagem do usuário no chat
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}  # Cria um dicionário para a mensagem do usuário
    st.session_state["lista_mensagens"].append(mensagem)  # Adiciona a mensagem do usuário ao histórico

    # resposta da IA
    # Gera uma resposta da IA com base no histórico de mensagens
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content  # Extrai o conteúdo da resposta da IA

    # Exibe a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}  # Cria um dicionário para a mensagem da IA
    st.session_state["lista_mensagens"].append(mensagem_ia)  # Adiciona a resposta da IA ao histórico