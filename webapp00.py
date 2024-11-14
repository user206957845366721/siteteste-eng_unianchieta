# MEU PRIMEIRO WEB APP
import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(
    page_title="Calculadora de Orçamentos",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': 'https://docs.streamlit.io',
        'About': "# Programação Engenharia Civil"
    }
)

with st.container():
    st.image("tech.jpg", use_column_width=True)
    
st.title("Bem-vindo/a!")
st.header("Calculadora de Orçamentos - Eng. Civil 2024")

st.markdown(
    """
    <style>
        .css-1m8jjsw edgvbvh3 {
        background-color: #135fa6; /COR FUNDO/
        color: white /COR TEXTO/
    }
    </style>
    """,
    unsafe_allow_html=True
)

data = st.file_uploader("Faça Upload da Lista.XLSX para envio em lote.", type=["xlsx"])
PressBotaoEnviaLISTA = st.button(label = '✔️ ENVIAR PARA LISTA')
if data is not None:
    df = pd.read_excel(data)   



#data = st.file_uploader("Carregue o seu orçamento aqui.", type=["xlsx", "xls"])
#if data is not None:
#    df = pd.read_excel(data) 
#    st.write(df)
#else:
#    st.write("Nenhum arquivo carregado.")

#cliente insere dados, que voltam como uma planilha do excel. gera arquivos. criar espaços para inserir dados.
