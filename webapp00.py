# MEU PRIMEIRO WEB APP
import streamlit as st
import pandas as pd
import numpy as np
import requests

with st.container():
    st.image("Programação Engenharia Civil.png", use_column_width='auto')

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem-vindo/a!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Site de Tabela de Orçamentos - Engenharia Civil 2024")

uploaded_file = st.file_uploader("Carregue o seu orçamento aqui.", type=["xlsx", "xls"])
if uploaded_file is not None:
    df = pd_read_excel(uploaded_file)
st.dataframe(df)




# Use st.write("") para adicionar um texto ao seu Web app

#usar excel. usar abas. cada aba tem dados de materiais, usar isso para comparar. e criar 3 pelo menos, das coisas que vamos usar
