# MEU PRIMEIRO WEB APP
import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(
    page_title="Calculadora de Orçamentos",
    page_icon="🖩",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': 'https://docs.streamlit.io',
        'About': "# Programação Engenharia Civil"
    }
)

with st.container():
    st.image("Programação Engenharia Civil.png", use_column_width='auto')
    
st.title("Bem-vindo/a!")
st.header("Calculadora de Orçamentos - Eng. Civil 2024")

uploaded_file = st.file_uploader("Carregue o seu orçamento aqui.", type=["xlsx", "xls"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
else:
    st.write("Nenhum arquivo carregado.")


#usar excel. usar abas. cada aba tem dados de materiais, usar isso para comparar. e criar 3 pelo menos, das coisas que vamos usar
