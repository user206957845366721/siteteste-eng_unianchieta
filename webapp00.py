# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem-vindo/a!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Site de Tabela de Orçamentos - Engenharia Civil 2024")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Selecione as opções desejadas na tabela abaixo:")

a = st.sidebar.radio("Selecione uma opção:", ["Gráfico", "Tabela Interativa"])
st.map(df)

# Use st.write("") para adicionar um texto ao seu Web app
