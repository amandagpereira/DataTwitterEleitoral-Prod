#comando para executar python3 app.py
import pandas as pd
import streamlit as st

st.title('Jornada além dos dados')

df = pd.read_csv("etapa4_dataframe_final.csv")

candidato_unico = sorted(df['Candidato'].unique())
selecionar_candidato = st.sidebar.multiselect('Candidato', candidato_unico, candidato_unico)

df_candidato_selecionado = df[df['Candidato'].isin(selecionar_candidato)]
st.dataframe(df_candidato_selecionado)


#print(df)
