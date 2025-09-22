# 🤖 ChatBot com IA - Streamlit + OpenAI

Este projeto implementa um **ChatBot interativo** utilizando **Streamlit** para frontend e backend, integrado com a **API da OpenAI** para gerar respostas inteligentes.  
O usuário pode enviar mensagens pelo chat e receber respostas em tempo real de um modelo de linguagem avançado.

Este projeto foi desenvolvido durante o curso **Jornada Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/), como forma de aplicar conceitos de **Python, Streamlit e APIs de Inteligência Artificial, além de estado de sessão, interação com o usuário e integração com modelos de IA**.

O projeto foi desenvolvido como parte do estudo de **Python, Streamlit e APIs de Inteligência Artificial**, aplicando conceitos de **estado de sessão, interação com usuário e integração com modelos de IA**.

---

## 📌 Sobre o Projeto

O sistema realiza automaticamente:

- 🖥️ **Interface de chat interativa** com Streamlit  
- 💬 **Armazenamento do histórico de mensagens** usando `st.session_state`  
- 🤖 **Geração de respostas com IA** através da API da OpenAI (`gpt-4o`)  
- 🔒 **Gerenciamento seguro da API Key** (não deve ser exposta publicamente)  
- ✅ **Atualização dinâmica do chat** exibindo mensagens do usuário e respostas do assistente  

---

## 🚀 Tecnologias Utilizadas

- **Python**  
- **Streamlit** – criação de interface web interativa  
- **OpenAI** – geração de respostas de linguagem natural  

---

## 📂 Estrutura do Projeto

- `main.py` – Script principal do chat  
- Dependências: `streamlit`, `openai`  

---

## ▶️ Como Usar

1. Clone o repositório e instale as dependências: pip install streamlit openai
2. Gere sua API Key no site da OpenAI, caso ainda não tenha.
3. No código, substitua "Digite sua chave API aqui" pela sua API Key pessoal.
   > Atenção: Se for publicar este projeto, não exponha sua chave. Use variáveis de ambiente ou arquivos .env para protegê-la.
4. Execute o aplicativo Streamlit: streamlit run main.py

---

## Contato

- Linkedin: [Neil Lopes](https://www.linkedin.com/in/neil-lopes-4a33a5383)
- E-mail: **neillopes237@gmail.com**
- Instagram: **neilzsz**

---

> Este projeto foi desenvolvido como parte do meu aprendizado em Python e IA, aplicando Streamlit e integração com APIs, contribuindo para a construção do meu portfólio profissional.
