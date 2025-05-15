import streamlit as st
import pandas as pd
import numpy as np

# Carregar os dados do Titanic'
df = pd.read_csv("./titanic3.csv", low_memory=False)

# Título do aplicativo
st.title("🚢 Dashboard Interativo do Titanic")

# 1. Visão Geral dos Dados
st.header("🔎 Visão Geral dos Dados")

# Número total de passageiros
total_passageiros = len(df)
st.metric(label="Total de Passageiros", value=total_passageiros)

# Taxa de sobrevivência geral
sobreviventes = df['survived'].value_counts(normalize=True) * 100
sobreviveu_pct = sobreviventes.get(1, 0)
nao_sobreviveu_pct = sobreviventes.get(0, 0)
st.metric(label="Taxa de Sobrevivência", value=f"{survived:.2f}%")
st.metric(label="Taxa de Mortalidade", value=f"{nao_sobreviveu_pct:.2f}%")

# Quantidade e percentual de dados ausentes
st.subheader("📉 Dados Ausentes")
missing_data = df.isna().sum()
missing_percent = (missing_data / len(df)) * 100
missing_df = pd.DataFrame({"Dados Ausentes": missing_data, "Percentual (%)": missing_percent})
st.dataframe(missing_df.sort_values(by="Percentual (%)", ascending=False))
