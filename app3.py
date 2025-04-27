# Importando as bibliotecas necessárias para manipulação de dados, visualização e criação da interface web
import pandas as pd  # Manipulação de dados em tabelas (DataFrames)
import numpy as np  # Operações numéricas e matemáticas
import matplotlib.pyplot as plt  # Geração de gráficos básicos
import seaborn as sns  # Gráficos estatísticos com estilo mais refinado
import streamlit as st  # Criação da interface interativa no navegador

# Função para carregar o arquivo de dados e realizar a limpeza dos nomes de coluna
def carregar_dados(uploaded_file):
    # Carrega o arquivo Excel enviado pelo usuário, utilizando a aba 'br_seeg_emissoes_brasil'
    df = pd.read_excel(uploaded_file, sheet_name='br_seeg_emissoes_brasil')
    # Remove espaços extras dos nomes das colunas, evitando erros futuros
    df.columns = df.columns.str.strip()
    return df

# Função para calcular a tabela de frequência da variável CH4
def calcular_frequencia(df):
    # Conta o número de observações (não nulos) da variável CH4
    n = df['CH4'].count()
    
    # Aplica a Regra de Sturges para determinar o número de intervalos de classe
    k = int(1 + 3.322 * np.log10(n))
    
    # Cria os limites dos intervalos de classe uniformemente espaçados
    intervalos = np.linspace(df['CH4'].min(), df['CH4'].max(), k + 1)
    
    # Classifica os dados de CH4 dentro dos intervalos de classe
    tabela_frequencia = pd.cut(df['CH4'], bins=intervalos, right=False, include_lowest=True)
    
    # Calcula a frequência absoluta (quantidade de observações por intervalo)
    frequencia_absoluta = tabela_frequencia.value_counts().sort_index()
    
    # Calcula a frequência relativa (proporção de cada intervalo em relação ao total)
    frequencia_relativa = frequencia_absoluta / n
    
    # Calcula a frequência acumulada (soma progressiva das frequências absolutas)
    frequencia_acumulada = frequencia_absoluta.cumsum()
    
    # Cria um DataFrame com todas as informações de frequência
    tabela_frequencia_df = pd.DataFrame({
        'Intervalo de Classe': frequencia_absoluta.index,
        'Frequência Absoluta': frequencia_absoluta.values,
        'Frequência Relativa': frequencia_relativa.values,
        'Frequência Acumulada': frequencia_acumulada.values
    })
    
    return tabela_frequencia_df

# Função para calcular as medidas descritivas da variável CH4
def calcular_medidas(df):
    # Cria um dicionário para armazenar várias medidas estatísticas básicas da coluna 'CH4'
    medidas = {
        'Número de Casos': df['CH4'].count(),  # Conta o número total de valores não nulos na variável CH4
        'Média': df['CH4'].mean(),             # Calcula a média aritmética dos valores da variável CH4
        'Mediana': df['CH4'].median(),         # Calcula a mediana (valor central) dos dados da variável CH4
        'Desvio Padrão': df['CH4'].std(),      # Calcula o desvio padrão, indicando a dispersão dos dados
        'Valor Máximo': df['CH4'].max(),       # Encontra o maior valor registrado na variável CH4
        'Valor Mínimo': df['CH4'].min()        # Encontra o menor valor registrado na variável CH4
    }
    
    # Converte o dicionário de medidas em um DataFrame (tabela) para facilitar a visualização no Streamlit
    medidas_df = pd.DataFrame(list(medidas.items()), columns=['Medida', 'Valor'])
    
    # Retorna o DataFrame contendo todas as medidas descritivas calculadas
    return medidas_df


# Função para criar o gráfico da distribuição das frequências absolutas
def criar_grafico(tabela_frequencia_df):
    # Define o tema visual do gráfico (fundo branco com linhas de grade)
    sns.set_theme(style="whitegrid")
    
    # Define o tamanho da figura
    plt.figure(figsize=(12, 6))
    
    # Cria o gráfico de barras usando Seaborn
    sns.barplot(
        x=tabela_frequencia_df['Intervalo de Classe'].astype(str),  # Converte intervalos para string para aparecerem no eixo X
        y=tabela_frequencia_df['Frequência Absoluta'],  # Frequência absoluta no eixo Y
        palette='Blues',  # Define uma paleta de cores em tons de azul
        edgecolor='black'  # Adiciona bordas pretas nas barras para melhor visualização
    )
    
    # Adiciona título e rótulos aos eixos
    plt.title('Distribuição das Frequências Absolutas', fontsize=16)
    plt.xlabel('Intervalos de Classe (CH4)', fontsize=12)
    plt.ylabel('Frequência Absoluta', fontsize=12)
    
    # Rotaciona os rótulos do eixo X para melhor leitura
    plt.xticks(rotation=45, ha='right')
    
    # Ajusta automaticamente o layout para não cortar os rótulos
    plt.tight_layout()
    
    # Exibe o gráfico no aplicativo Streamlit
    st.pyplot(plt)

# Função principal que organiza a execução da aplicação no Streamlit
def main():
    # Define o título da página
    st.title('📊 Análise Estatística da Emissão de Gases na Produção de Arroz')
    
    # Exibe uma breve descrição da aplicação
    st.markdown("""
    Este aplicativo realiza uma análise estatística das emissões de metano (CH4) na produção de arroz.
    Faça o upload de uma planilha `.xlsx` com os dados para iniciar a análise.
    """)

    # Cria o componente de upload de arquivo no Streamlit
    uploaded_file = st.file_uploader("📂 Escolha uma planilha .xlsx", type="xlsx")
    
    # Verifica se o arquivo foi carregado
    if uploaded_file is not None:
        # Carrega os dados do arquivo
        df = carregar_dados(uploaded_file)
        
        # Exibe as primeiras linhas dos dados carregados
        st.subheader('📄 Dados Carregados')
        st.dataframe(df.head())
        
        # Calcula a tabela de frequência
        tabela_frequencia_df = calcular_frequencia(df)
        
        # Exibe a tabela de frequência
        st.subheader('📈 Tabela de Frequência')
        st.dataframe(tabela_frequencia_df)
        
        # Gera e exibe o gráfico de barras
        st.subheader('📊 Gráfico da Distribuição das Frequências Absolutas')
        criar_grafico(tabela_frequencia_df)
        
        # Calcula as medidas descritivas
        medidas_df = calcular_medidas(df)
        
        # Exibe as medidas descritivas
        st.subheader('📚 Medidas Descritivas')
        st.dataframe(medidas_df)

# Verifica se o script está sendo executado diretamente e chama a função principal
if __name__ == "__main__":
    main()

