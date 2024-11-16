# MEU PRIMEIRO WEB APP
import streamlit as st
import pandas as pd
import numpy as np
import requests
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

#POSSIBILITAR CARREGAMENTO DE PLANILHA
def carregar_planilha():
    uploaded_file = st.file_uploader("Carregue sua planilha aqui:", type=["xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        st.write("Produtos carregados:", df)
        return df
    else:
        st.warning("Por favor, carregue uma planilha do Excel.")
    return None

#SELECIONAR PRODUTOS
def selecionar_produtos(df):
    if df is not None:
        produtos_disponiveis = df['DESCRIÇÃO'].tolist()
        produtos_selecionados = st.multiselect("Selecione os produtos", produtos_disponiveis)
        df_selecionados = df[df['DESCRIÇÃO'].isin(produtos_selecionados)]
        return df_selecionados
    else:
        return pd.DataFrame()

#ADD PREÇOS E DESCONTO
def adicionar_preços_DESCONTO(df):
    if df is not None:
        for index, row in df.iterrows():
            with st.expander(f"Produto: {row['DESCRIÇÃO']}"):
                preço = st.number_input(f"Preço de {row['DESCRIÇÃO']}", min_value=0.0, value=row['R$'], key=f"preço_{index}")
                desconto = st.number_input(f"Desconto (%) para {row['DESCRIÇÃO']}", min_value=0.0, max_value=100.0, value=row['DESCONTO'], key=f"desconto_{index}")
                df.at[index, 'R$'] = preço
                df.at[index, 'DESCONTO'] = desconto
        return df
    else:
        return pd.DataFrame()

#CALCULAR ORÇAMENTO
def calcular_orçamento(df_com_preços):
    total = 0
    for index, row in df_com_preços.iterrows():
        preço_com_desconto = row['R$'] * (1 - row['DESCONTO'] / 100)
        df.at[index, 'Preço com desconto'] = preço_com_desconto
        total += preço_com_desconto
    return df_com_preços, total

#PROCESSO PARA GERAR O PDF DO ORÇAMENTO
def gerar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Orçamento de Produtos", ln=True, align='C')

    pdf.ln(10)
    pdf.cell(40, 10, row['DESCRIÇÃO'], border=1)
    pdf.cell(40, 10, f"R$ {row['R$']:.2f}", border=1)
    pdf.cell(40, 10, f"{row['DESCONTO']}%", border=1)
    pdf.cell(40, 10, f"R$ {row['Preço com desconto']:.2f}", border=1)
    pdf.ln()

    buffer=BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer
def main():
    st.title("Calculadora de Orçamento")

    # Carregar a planilha de produtos
    df = carregar_planilha()

    if df is not None:
        # Selecionar os produtos
        df_selecionados = selecionar_produtos(df)
        
        # Adicionar preços e descontos aos produtos
        df_com_preços = adicionar_preços_descontos(df_selecionados)
        
        # Calcular o total do orçamento
        df_com_preços, total = calcular_orçamento(df_com_preços)

        # Exibir o orçamento calculado
        st.write("Orçamento Calculado:")
        st.dataframe(df_com_preços)

        # Botão para gerar o PDF do orçamento
        if st.button("Gerar Orçamento em PDF"):
            buffer_pdf = gerar_pdf(df_com_preços, total)
            st.download_button(
                label="Baixar Orçamento em PDF",
                data=buffer_pdf,
                file_name="orcamento.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()

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
