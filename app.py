import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Função para carregar o arquivo de dados
def carregar_dados(uploaded_file):
    # Carregar o arquivo Excel
    df = pd.read_excel(uploaded_file, sheet_name='br_seeg_emissoes_brasil')
    return df

# Função para calcular a tabela de frequência
def calcular_frequencia(df):
    n = df['CH4'].count()
    k = int(1 + 3.322 * np.log10(n))  # Regra de Sturges
    
    intervalos = np.linspace(df['CH4'].min(), df['CH4'].max(), k+1)
    tabela_frequencia = pd.cut(df['CH4'], bins=intervalos, right=False, include_lowest=True)
    
    frequencia_absoluta = tabela_frequencia.value_counts().sort_index()
    frequencia_relativa = frequencia_absoluta / n
    frequencia_acumulada = frequencia_absoluta.cumsum()
    
    tabela_frequencia_df = pd.DataFrame({
        'Intervalo de Classe': frequencia_absoluta.index,
        'Frequência Absoluta': frequencia_absoluta.values,
        'Frequência Relativa': frequencia_relativa.values,
        'Frequência Acumulada': frequencia_acumulada.values
    })
    
    return tabela_frequencia_df

# Função para calcular as medidas descritivas
def calcular_medidas(df):
    medidas = {
        'Número de Casos': df['CH4'].count(),
        'Média': df['CH4'].mean(),
        'Mediana': df['CH4'].median(),
        'Desvio Padrão': df['CH4'].std(),
        'Valor Máximo': df['CH4'].max(),
        'Valor Mínimo': df['CH4'].min()
    }

    # Converting the measures into a DataFrame for better visualization in Streamlit
    medidas_df = pd.DataFrame(list(medidas.items()), columns=['Medida', 'Valor'])
    
    return medidas_df

# Função para criar o gráfico de colunas
def criar_grafico(tabela_frequencia_df):
    plt.figure(figsize=(10, 6))
    tabela_frequencia_df['Frequência Absoluta'].plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribuição das Frequências Absolutas', fontsize=16)
    plt.xlabel('Intervalos de Classe', fontsize=12)
    plt.ylabel('Frequência Absoluta', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

# Interface do Streamlit
def main():
    st.title('Análise Estatística da Emissão de Gases na Produção de Arroz')

    st.markdown("""
    Este aplicativo permite realizar uma análise estatística da emissão de gases na produção de arroz, com base em dados de emissão de CH4. O usuário pode fazer upload de uma planilha `.xlsx` contendo os dados para análise.
    """)
    
    # Upload do arquivo
    uploaded_file = st.file_uploader("Escolha uma planilha .xlsx", type="xlsx")
    
    if uploaded_file is not None:
        # Carregar os dados
        df = carregar_dados(uploaded_file)
        
        # Exibir os dados carregados
        st.subheader('Dados Carregados')
        st.write(df.head())
        
        # Calcular a tabela de frequência
        tabela_frequencia_df = calcular_frequencia(df)
        
        # Exibir a tabela de frequência
        st.subheader('Tabela de Frequência')
        st.write(tabela_frequencia_df)
        
        # Exibir o gráfico de colunas
        st.subheader('Gráfico de Frequências Absolutas')
        criar_grafico(tabela_frequencia_df)
        
        # Calcular as medidas descritivas
        medidas_df = calcular_medidas(df)
        
        # Exibir as medidas descritivas em formato de tabela
        st.subheader('Medidas Descritivas')
        st.write(medidas_df)

# Rodar o aplicativo
if __name__ == "__main__":
    main()

