# MEU PRIMEIRO WEB APP
import streamlit as st


st.logo("Programação Engenharia Civil.png")
st.image("./Programação Engenharia Civil.png")
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem-vindo/a!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Site de Tabela de Orçamentos - Engenharia Civil 2024")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Selecione as opções desejadas na tabela abaixo:")

st.selectbox("Selecione uma opção:", ["Tabela", "Gráfico"])

a = st.sidebar.radio("Teste", [teste])


# Use st.write("") para adicionar um texto ao seu Web app
