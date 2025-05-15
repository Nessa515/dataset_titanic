import pandas as pd
import streamlit as st

# Carregar o arquivo CSV
if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv('./titanic3.csv', low_memory=False)

df = st.session_state['df_titanic']

# Mostrar o total de passageiros
df.head()
