# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem-vindo/a!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Site de Tabela de Orçamentos - Engenharia Civil 2024")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Selecione as opções desejadas na tabela abaixo:")

col1, col2 = st.columns(2)
col1.write("Teste 1")
col2.write("Teste 2")

# Use st.write("") para adicionar um texto ao seu Web app
