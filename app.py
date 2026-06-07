import pandas as pd 
import streamlit as st
import plotly.express as px # type: ignore

st.title('Dashboard — Mercado de TI 2024')

df = pd.read_csv('data/results.csv')
st.write(f'Dataset carregado: {df.shape[0]} linhas e {df.shape[1]} colunas')

colunas = [
    'LanguageHaveWorkedWith',
    'ConvertedCompYearly',
    'DevType',
    'RemoteWork',
    'Country'
]

df_filtrado = df[colunas].copy()

st.sidebar.header('Filtros')
paises = df_filtrado['Country'].dropna().unique()
pais_selecionado = st.sidebar.selectbox('Selecione um país', sorted(paises))
df_filtrado = df_filtrado[df_filtrado['Country'] == pais_selecionado]

st.header('Top 10 Linguagens Mais Usadas')

linguagens = df_filtrado['LanguageHaveWorkedWith'].dropna()
todas = linguagens.str.split(';').explode()
top10 = todas.value_counts().head(10).reset_index()
top10.columns = ['Linguagem', 'Quantidade']

fig = px.bar(top10, x='Quantidade', y='Linguagem', orientation='h', title='Top 10 Linguagens')
st.plotly_chart(fig)

st.header('Modalidade de Trabalho')

remoto = df_filtrado['RemoteWork'].dropna()
remoto = remoto.value_counts().reset_index()
remoto.columns = ['Remote', 'Quantidade']

fig = px.bar(remoto, x='Quantidade', y='Remote', orientation='h', title='Modalidade de Trabalho')
st.plotly_chart(fig)

st.header('Distribuição Salarial')
salarios = df_filtrado['ConvertedCompYearly'].dropna()
fig = px.histogram(salarios, x='ConvertedCompYearly', nbins=50, title='Distribuição Salarial')
st.plotly_chart(fig)