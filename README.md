# Análise Estatística da Emissão de Gases na Produção de Arroz

## Descrição

Este projeto visa realizar uma análise estatística de dados sobre a **emissão de gases** na produção de arroz, especificamente o gás **metano (CH4)**. O aplicativo interativo, desenvolvido com a biblioteca **Streamlit**, permite ao usuário carregar uma planilha Excel contendo dados de emissão de gases e realizar a análise com base em cálculos estatísticos, como **tabelas de frequência** e **medidas descritivas**. O gráfico gerado oferece uma visualização clara da distribuição das emissões de **CH4**, e as medidas descritivas fornecem uma visão detalhada das características estatísticas dos dados.

## Funcionalidades

- **Upload de Arquivo**: O usuário pode carregar uma planilha `.xlsx` com os dados de emissões de gases.
- **Tabela de Frequência**: Cálculo das frequências absolutas, relativas e acumuladas para a variável **CH4**.
- **Gráfico Interativo**: Exibição de um gráfico de colunas que representa a distribuição das frequências absolutas.
- **Medidas Descritivas**: Cálculo de estatísticas como média, mediana, desvio padrão, valor máximo e valor mínimo.
  
## Tecnologias Usadas

- **[Streamlit](https://streamlit.io/)**: Framework para criação de interfaces web interativas.
- **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulação e análise de dados.
- **[Matplotlib](https://matplotlib.org/)**: Biblioteca para criação de gráficos e visualizações.
- **[NumPy](https://numpy.org/)**: Biblioteca para cálculos matemáticos.

## Como Executar Localmente

Para rodar este projeto em sua máquina local, siga as instruções abaixo:

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local com o comando:
```bash
git clone https://github.com/SEU_USUARIO/analise-emissao-gases-arroz.git
```
### 2. Navegar até o Diretório do Projeto
Entre no diretório do projeto:
```bash
cd analise-emissao-gases-arroz
```
### 3. Criar e Ativar um Ambiente Virtual (Opcional)
É altamente recomendado usar um ambiente virtual para evitar conflitos de dependências. Você pode criar um ambiente virtual com:
```bash
python -m venv venv
```
E ativá-lo com:
### Windows:
```bash
venv\Scripts\activate
```
### Linux/Mac:

```bash
source venv/bin/activate
```
### 4. Instalar as Dependências
Instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```
### Se o arquivo requirements.txt não existir, instale as dependências manualmente com:
```bash
pip install streamlit pandas matplotlib numpy openpyxl
```

### 5. Executar o Aplicativo Streamlit
Para iniciar o aplicativo localmente, execute o seguinte comando no terminal:
```bash
streamlit run app.py
```
Isso abrirá o aplicativo no seu navegador. Você poderá fazer upload de uma planilha .xlsx e ver as análises em tempo real.

### 6. Como Hospedar no Streamlit Cloud
Para hospedar este projeto na nuvem usando Streamlit Cloud, siga as etapas abaixo:

### 6.1. Conectar o GitHub ao Streamlit Cloud
Faça login em Streamlit Cloud.

Clique em "New app" e, em seguida, selecione GitHub para autenticar sua conta GitHub.

Escolha o repositório analise-emissao-gases-arroz e o arquivo app.py.

Clique em "Deploy" para criar e hospedar o aplicativo.

### 6.2. Acessar o Link
Após o Streamlit Cloud processar a aplicação, você receberá um link único que pode ser compartilhado com outros usuários para que acessem seu aplicativo diretamente pela web.

### Passo 7: Conectar o GitHub ao Streamlit Cloud
* Vá para o Streamlit Cloud.
* Faça login na sua conta ou crie uma conta gratuita.
* No dashboard do Streamlit Cloud, clique em "New app".
* Conecte sua conta GitHub e selecione o repositório analise-emissao-gases-arroz.
* Escolha o arquivo app.py como o ponto de entrada para o aplicativo.
* Clique em "Deploy" para iniciar o aplicativo.
* Após alguns minutos, o Streamlit Cloud criará e hospedará o seu aplicativo. O link gerado será fornecido, e você poderá compartilhá-lo com outras pessoas para acessarem a aplicação interativa.
