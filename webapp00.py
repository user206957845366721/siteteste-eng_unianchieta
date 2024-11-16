# MEU PRIMEIRO WEB APP
import streamlit as st
import pandas as pd
import numpy as np
import requests
from io import BytesIO
from fpdf import FPDF

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

produtos = [
    {"id": 1, "nome": "Produto A", "preço": "0.0, "desconto": 0.0},
    {"id": 2, "nome": "Produto B", "preço": "0.0, "desconto": 0.0},
    {"id": 3, "nome": "Produto C", "preço": "0.0, "desconto": 0.0},
]

df = pd.DataFrame(produtos)
st.write("Tabela de Produtos:"
df_display = st.dataframe(df)

#data = st.file_uploader("Faça Upload da Lista.XLSX para envio em lote.", type=["xlsx", "xls"])
#PressBotaoEnviaLISTA = st.button(label = '✔️ ENVIAR PARA LISTA')
#if data is not None:
#    df = pd.read_excel(data)   
#    st.write(df)
#    df.columns = ['C1','C2','C3','C4','C5','C6','C7','C8','C9']
#    st.write(df.columns)
#    st.write(df)


#data = st.file_uploader("Carregue o seu orçamento aqui.", type=["xlsx", "xls"])
#if data is not None:
#    df = pd.read_excel(data) 
#    st.write(df)
#else:
#    st.write("Nenhum arquivo carregado.")

#cliente insere dados, que voltam como uma planilha do excel. gera arquivos. criar espaços para inserir dados.
