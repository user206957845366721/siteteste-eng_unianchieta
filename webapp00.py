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

for index, row in df.iterrows():
    with st.form(f"form_{row['id]}"):
        st.write(f"Produto: {row['nome']}")
        preço = st.number_input(f"Preço de {row['nome']}", min_value=0.0, step=0.01, key=f"preço_{row['id']}")
        desconto = st.number_input(f"Desconto (%) para {row['nome']}", min _value=0.0, max_value=100.0, step=0.01, key=f"desconto_{row['id']}")

        submit_button = st.form_submit_button(label="Atualizar")

        if submit_button:
            df.at[index, 'preço'] = preço
            df.at[index, 'desconto'] = desconto
            
st.write("Tabela Atualizada")
st.dataframe(df)

def calcular_valor_total(df):
    total = 0.0
    for index, row in df.interrows():
        valor_com_desconto = row['preço'] * (1 - row['desconto'] / 100)
        total += valor_com_desconto
    return total

total = calcular_valor_total(df)
st.write(f"Valor Total: R$ {total:.2f}")

def gerar_pdf(df, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Orçamento de Produtos", ln=True, align='C')

    pdf.ln(10)
    pdf.cell(40, 10, "Produto", border=1)
    pdf.cell(40, 10, "Preço", border=1)
    pdf.cell(40, 10, "Desconto (%)", border=1)
    pdf.cell(40, 10, "Preço Final", border=1)
    pdf.ln()

    for index, row in df.iterrows():
        preço_final = row['preço'] * (1 - row['desconto'] / 100)
        pdf.cell(40, 10, row['nome'], border=1)
        pdf.cell(40, 10, f"R$ {row['preço']:.2f}", border=1)
        pdf.cell(40, 10, f"{row['desconto']}%", border=1)
        pdf.cell(40, 10, f"R$ {preço_final:.2f}", border=1)
        pdf.ln()

    pdf.ln(10)
    pdf.cell(40, 10, f"Total: R$ {total:.2f}", ln=True)

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

if st.button("Gerar documento em PDF"):
    buffer_pdf = gerar_pdf(df, total)
    st.download_button(
        label ="Baixar orçamento em PDF",
        data=buffer.pdf,
        file_name="orçamento.pdf",
        mime="application/pdf"
    )

    

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
