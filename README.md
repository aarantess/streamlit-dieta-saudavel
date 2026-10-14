# 🥗 Custo de uma Dieta Saudável

Dashboard interativo desenvolvido em **Python e Streamlit** para explorar indicadores relacionados ao custo e à acessibilidade de uma dieta saudável em diferentes países e regiões.

🔗 **Acesse o dashboard:**  
https://app-dieta-saudavel.streamlit.app/

---

## 📊 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de transformar uma base de dados sobre o **custo de uma dieta saudável** em uma aplicação web interativa, permitindo explorar os dados de forma simples e visual.

A aplicação possibilita analisar diferentes indicadores, países, períodos e unidades de medida, facilitando a comparação e a identificação da evolução dos dados ao longo do tempo.

Além da análise de dados, o projeto também colocou em prática o fluxo completo de desenvolvimento e publicação de uma aplicação:

**Python → Git → GitHub → Streamlit Community Cloud**

---

## 🔎 Funcionalidades

O dashboard permite:

- Selecionar diferentes indicadores para análise;
- Filtrar países e regiões;
- Selecionar o período desejado;
- Comparar até 8 países ou regiões;
- Visualizar indicadores resumidos por meio de KPIs;
- Analisar a evolução dos valores ao longo do tempo;
- Comparar países por meio de gráficos interativos;
- Trabalhar com diferentes unidades de medida;
- Visualizar os dados filtrados em tabela;
- Exportar os dados selecionados em formato CSV.

---

## 📈 Visualizações

A aplicação possui diferentes áreas de análise:

### Visão Geral

Apresenta os principais indicadores da seleção realizada pelo usuário, permitindo uma leitura rápida do cenário analisado.

### Gráficos

Permite acompanhar a evolução temporal dos indicadores e realizar comparações entre os países ou regiões selecionados.

### Dados

Exibe os registros utilizados na análise e permite baixar os dados filtrados em formato CSV.

---

## 🗂️ Base de dados

O projeto utiliza o arquivo:

`Custo_Dieta_Saudavel_Traduzido_Completo.csv`

A base contém informações relacionadas a indicadores de custo e acessibilidade de uma dieta saudável, organizadas por país ou região e ano.

Entre os principais campos utilizados estão:

- País/Região;
- Indicador analisado;
- Ano;
- Unidade;
- Valor;
- Status do dado;
- Publicação.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas** — manipulação e tratamento dos dados
- **Plotly** — criação dos gráficos interativos
- **Streamlit** — desenvolvimento da aplicação web
- **Git** — controle de versão
- **GitHub** — armazenamento e versionamento do projeto
- **Streamlit Community Cloud** — publicação da aplicação

---

## 📁 Estrutura do projeto

```text
streamlit-dieta-saudavel/
│
├── app.py
├── Custo_Dieta_Saudavel_Traduzido_Completo.csv
├── requirements.txt
├── README.md
└── .gitignore