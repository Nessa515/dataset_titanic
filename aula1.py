import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_csv('titanic3.csv', sep=";", low_memory=False)

df = st.session_state['df']

# Sidebar Filters
st.sidebar.title('Filtros')
selected_sex = st.sidebar.multiselect('Sexo', options=['male', 'female'], default=[])
selected_pclass = st.sidebar.multiselect('Classe', options=[1, 2, 3], default=[])
selected_survived = st.sidebar.multiselect('Sobreviveu', options=[0, 1], default=[])

# Applying filters
filtered_df = df[(df['sex'].isin(selected_sex)) &
                 (df['pclass'].isin(selected_pclass)) &
                 (df['survived'].isin(selected_survived))]

# Visão Geral dos Dados
st.title('Análise do Titanic - Sobreviventes')

# Total de passageiros
st.subheader('Total de passageiros:')
st.write(len(df))

# Taxa de sobrevivência
survival_rate = df['survived'].value_counts(normalize=True) * 100
st.subheader('Taxa de Sobrevivência:')
st.write(f"Sobreviveram: {survival_rate[1]:.2f}%")
st.write(f"Não sobreviveram: {survival_rate[0]:.2f}%")

# Dados ausentes
st.subheader('Dados Ausentes:')
missing_data = df.isna().sum()
missing_percent = (missing_data / len(df)) * 100
st.write(pd.DataFrame({'Total de Dados Ausentes': missing_data, 'Percentual (%)': missing_percent}))

# Análises Visuais
st.subheader('Análises Visuais')

# Gráfico de sobrevivência por sexo
fig1 = px.bar(filtered_df.groupby('sex')['survived'].mean().reset_index(), x='sex', y='survived', title='Taxa de Sobrevivência por Sexo')
st.plotly_chart(fig1)

# Gráfico de sobrevivência por classe
fig2 = px.bar(filtered_df.groupby('pclass')['survived'].mean().reset_index(), x='pclass', y='survived', title='Taxa de Sobrevivência por Classe')
st.plotly_chart(fig2)

# Gráfico de Idade vs Sobrevivência (Boxplot)
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x='survived', y='age', ax=ax)
ax.set_title('Idade vs Sobrevivência')
st.pyplot(fig)

# Dados ausentes destacados
st.subheader('Impacto dos Dados Ausentes')
st.write('Analisando o impacto de dados ausentes nas variáveis-chave:')
st.write(filtered_df.isna().sum())

