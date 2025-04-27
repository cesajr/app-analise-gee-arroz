# Importando as bibliotecas necessárias para manipulação de dados, visualização e criação da interface web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Função para carregar o arquivo de dados e realizar a limpeza dos nomes de coluna
def carregar_dados(uploaded_file):
    df = pd.read_excel(uploaded_file, sheet_name='br_seeg_emissoes_brasil')
    df.columns = df.columns.str.strip()
    return df

# Função para calcular a tabela de frequência da variável CH4
def calcular_frequencia(df):
    n = df['CH4'].count()  # Número de observações (não nulos)
    k = int(1 + 3.322 * np.log10(n))  # Número de classes (Regra de Sturges)
    
    intervalos = np.linspace(df['CH4'].min(), df['CH4'].max(), k + 1)  # Criação dos intervalos de classe
    tabela_frequencia = pd.cut(df['CH4'], bins=intervalos,
                               right=False, include_lowest=True)  # Classificação dos dados nos intervalos
    
    frequencia_absoluta = tabela_frequencia.value_counts().sort_index()
    frequencia_relativa = frequencia_absoluta / n
    frequencia_acumulada = frequencia_absoluta.cumsum()
    
    tabela_frequencia_df = pd.DataFrame({
        'Intervalo de Classe': frequencia_absoluta.index,
        'Frequência Absoluta': frequencia_absoluta.values,
        'Frequência Relativa': frequencia_relativa.values,
        'Frequência Acumulada': frequencia_acumulada.values
    })
    
    return tabela_frequencia_df, k  # Agora também retorna o número de classes

# Função para calcular as medidas descritivas da variável CH4
def calcular_medidas(df):
    medidas = {
        'Número de Casos': df['CH4'].count(),
        'Média': df['CH4'].mean(),
        'Mediana': df['CH4'].median(),
        'Desvio Padrão': df['CH4'].std(),
        'Valor Máximo': df['CH4'].max(),
        'Valor Mínimo': df['CH4'].min()
    }
    medidas_df = pd.DataFrame(list(medidas.items()), columns=['Medida', 'Valor'])
    return medidas_df

# Função para criar o gráfico da distribuição das frequências absolutas
def criar_grafico(tabela_frequencia_df):
    sns.set_theme(style="whitegrid")  # Tema visual
    
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=tabela_frequencia_df['Intervalo de Classe'].astype(str),
        y=tabela_frequencia_df['Frequência Absoluta'],
        palette='Blues',
        edgecolor='black'
    )
    plt.title('Distribuição das Frequências Absolutas', fontsize=16)
    plt.xlabel('Intervalos de Classe (CH4)', fontsize=12)
    plt.ylabel('Frequência Absoluta', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

# Interface principal da aplicação
def main():
    st.title('📊 Análise Estatística da Emissão de Gases na Produção de Arroz')

    st.markdown("""
    Este aplicativo realiza uma análise estatística das emissões de metano (CH4) na produção de arroz.
    Faça o upload de uma planilha `.xlsx` com os dados para iniciar a análise.
    """)

    uploaded_file = st.file_uploader("📂 Escolha uma planilha .xlsx", type="xlsx")
    
    if uploaded_file is not None:
        df = carregar_dados(uploaded_file)
        
        st.subheader('📄 Dados Carregados')
        st.dataframe(df.head())

        # Calcular a tabela de frequência e capturar também o número de classes
        tabela_frequencia_df, k = calcular_frequencia(df)
        
        # Exibir o número de classes definidas pela Regra de Sturges
        st.subheader('📐 Número de Classes - Regra de Sturges')
        st.markdown(f"O número de **intervalos de classe** determinado pela Regra de Sturges: **{k}**.", unsafe_allow_html=True)
        
        # Exibir a tabela de frequência
        st.subheader('📈 Tabela de Frequência')
        st.dataframe(tabela_frequencia_df)

        # Exibir o gráfico de colunas
        st.subheader('📊 Gráfico da Distribuição das Frequências Absolutas')
        criar_grafico(tabela_frequencia_df)

        # Calcular as medidas descritivas
        medidas_df = calcular_medidas(df)

        # Exibir as medidas descritivas
        st.subheader('📚 Medidas Descritivas')
        st.dataframe(medidas_df)

# Rodar o aplicativo
if __name__ == "__main__":
    main()
