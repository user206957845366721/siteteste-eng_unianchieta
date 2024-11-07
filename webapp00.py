# MEU PRIMEIRO WEB APP
import streamlit as st
import pandas as pd
import numpy as np
import requests

with st.container():
    st.image("Programação Engenharia Civil.png")

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem-vindo/a!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Site de Tabela de Orçamentos - Engenharia Civil 2024")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Selecione as opções desejadas abaixo:")

df1 = pd.DataFrame(np.random.randn(5, 5), columns=("col %d" % i for i in range(5)))
df2 = pd.DataFrame(np.random.randn(10,5), columns=("col %d" % i for i in range(10)))
                

left, right = st.columns(2)
if left.button("Tabela", use_container_width=True):
    left.markdown(st.dataframe(df1))
if right.button("Gráfico", icon=":material/mood:", use_container_width=True):
    right.markdown(st.dataframe(df2))

# Use st.write("") para adicionar um texto ao seu Web app
