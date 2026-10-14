from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Custo de uma Dieta Saudável",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# IDENTIDADE VISUAL
# ============================================================

VERDE = "#146B4A"
VERDE_ESCURO = "#0D5238"
VERDE_MEDIO = "#2F8A63"
VERDE_CLARO = "#EAF6F0"
FUNDO = "#F8FAF9"
TEXTO = "#15352D"
CINZA = "#66756F"
BORDA = "#E2EAE6"

PALETA = [
    "#146B4A",
    "#67B99A",
    "#457B9D",
    "#B08968",
    "#7A9E9F",
    "#8F6D8A",
    "#A3B18A",
    "#6C757D",
]


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------
       PÁGINA
    -------------------------------- */

    .stApp {
        background-color: #F8FAF9;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.8rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #15352D;
        letter-spacing: -0.025em;
    }

    p {
        color: #52635D;
    }


    /* --------------------------------
       SIDEBAR
    -------------------------------- */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #F0F8F4 0%,
                #F8FBF9 100%
            );

        border-right: 1px solid #DCE9E2;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }


    /* --------------------------------
       MARCA DA SIDEBAR
    -------------------------------- */

    .sidebar-brand {
        padding: 6px 4px 20px 4px;
    }

    .sidebar-brand-title {
        color: #0D5238;
        font-size: 23px;
        line-height: 1.15;
        font-weight: 750;
        margin-bottom: 12px;
    }

    .sidebar-brand-text {
        color: #52635D;
        font-size: 13.5px;
        line-height: 1.55;
    }


    /* --------------------------------
       CARD SOBRE PROJETO
    -------------------------------- */

    .sobre-projeto {
        background: #E3F3EA;
        border: 1px solid #CCE8D9;
        border-radius: 12px;
        padding: 16px;
        margin-top: 24px;
        color: #36594B;
        font-size: 13px;
        line-height: 1.5;
    }

    .sobre-projeto strong {
        color: #0D5238;
        font-size: 14px;
    }


    /* --------------------------------
       CAMPOS
    -------------------------------- */

    div[data-baseweb="select"] > div {
        border-radius: 9px;
    }

    div[data-testid="stSlider"] {
        padding-top: 4px;
    }


    /* --------------------------------
       KPIs
    -------------------------------- */

    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E2EAE6;
        padding: 18px 20px;
        border-radius: 12px;
        min-height: 125px;
        box-shadow:
            0 2px 8px rgba(24, 65, 51, 0.04);
    }

    div[data-testid="stMetricLabel"] {
        color: #52635D;
    }

    div[data-testid="stMetricValue"] {
        color: #15352D;
        font-weight: 700;
    }


    /* --------------------------------
       ABAS
    -------------------------------- */

    div[data-baseweb="tab-list"] {
        gap: 4px;
        border-bottom: 1px solid #E2EAE6;
    }

    button[data-baseweb="tab"] {
        font-size: 15px;
        font-weight: 600;
        padding-left: 24px;
        padding-right: 24px;
        border-radius: 8px 8px 0 0;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #146B4A;
        background: #EEF7F2;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #146B4A;
    }


    /* --------------------------------
       CONTEXTO
    -------------------------------- */

    .contexto-analise {
        background:
            linear-gradient(
                90deg,
                #E9F6F0,
                #F3F9F6
            );

        border: 1px solid #DCEEE5;
        border-radius: 11px;
        padding: 15px 18px;
        margin-top: 10px;
        margin-bottom: 22px;

        color: #36594B;
        font-size: 13.5px;
        line-height: 1.7;
    }

    .contexto-analise strong {
        color: #15352D;
    }


    /* --------------------------------
       GRÁFICOS
    -------------------------------- */

    div[data-testid="stPlotlyChart"] {
        background: #FFFFFF;
        border: 1px solid #E2EAE6;
        border-radius: 12px;
        padding: 10px;
        box-shadow:
            0 2px 8px rgba(24, 65, 51, 0.035);
    }


    /* --------------------------------
       DATAFRAME
    -------------------------------- */

    div[data-testid="stDataFrame"] {
        border: 1px solid #E2EAE6;
        border-radius: 10px;
        overflow: hidden;
    }


    /* --------------------------------
       BOTÕES
    -------------------------------- */

    div.stButton > button,
    div.stDownloadButton > button {
        background-color: #146B4A;
        color: #FFFFFF;
        border: 1px solid #146B4A;
        border-radius: 8px;
        font-weight: 650;
        min-height: 42px;
    }

    div.stButton > button:hover,
    div.stDownloadButton > button:hover {
        background-color: #0D5238;
        color: #FFFFFF;
        border-color: #0D5238;
    }


    /* --------------------------------
       EXPANDER
    -------------------------------- */

    div[data-testid="stExpander"] {
        background: #FFFFFF;
        border: 1px solid #E2EAE6;
        border-radius: 10px;
    }


    /* --------------------------------
       DIVISORES
    -------------------------------- */

    hr {
        border-color: #E2EAE6;
    }


    /* --------------------------------
       RODAPÉ
    -------------------------------- */

    .rodape {
        text-align: center;
        color: #84918C;
        font-size: 12px;
        padding: 8px 0 4px 0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CAMINHO DO ARQUIVO
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = (
    BASE_DIR
    / "Custo_Dieta_Saudavel_Traduzido_Completo.csv"
)


# ============================================================
# NOMES AMIGÁVEIS DAS UNIDADES
# ============================================================

NOMES_UNIDADES = {

    "Int$ (Paridade do Poder de Compra) por pessoa por dia":
        "Int$ (PPP) / pessoa / dia",

    "USD/capita/dia":
        "US$ / pessoa / dia",

    "Percentual":
        "%",

    "Milhões":
        "milhões de pessoas",
}


def nome_unidade_exibicao(unidade):

    return NOMES_UNIDADES.get(
        unidade,
        unidade
    )


# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

@st.cache_data(show_spinner=False)
def carregar_dados(caminho: Path) -> pd.DataFrame:

    dados = pd.read_csv(caminho)

    colunas_esperadas = {
        "Pais_Regiao",
        "Item_Analise",
        "Ano",
        "Unidade",
        "Valor",
        "Status_Dado",
        "Publicacao",
    }

    ausentes = colunas_esperadas.difference(
        dados.columns
    )

    if ausentes:

        raise ValueError(
            "O CSV não contém as colunas obrigatórias: "
            + ", ".join(sorted(ausentes))
        )

    dados["Ano"] = pd.to_numeric(
        dados["Ano"],
        errors="coerce"
    ).astype("Int64")

    dados["Valor"] = pd.to_numeric(
        dados["Valor"],
        errors="coerce"
    )

    dados = dados.dropna(
        subset=["Ano"]
    )

    return dados


# ============================================================
# FORMATAÇÃO DE VALORES
# ============================================================

def formatar_valor(valor, unidade):

    if pd.isna(valor):
        return "—"

    unidade_exibicao = (
        nome_unidade_exibicao(unidade)
    )

    if unidade_exibicao == "%":

        return (
            f"{valor:,.1f}%"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

    texto = (
        f"{valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

    if "milhões" in unidade_exibicao.lower():
        texto += " mi"

    return texto


# ============================================================
# VARIAÇÃO
# ============================================================

def calcular_variacao_percentual(
    valor_atual,
    valor_anterior
):

    if (
        pd.isna(valor_atual)
        or pd.isna(valor_anterior)
        or valor_anterior == 0
    ):
        return None

    return (
        (valor_atual - valor_anterior)
        / valor_anterior
    ) * 100


# ============================================================
# GRÁFICO DE EVOLUÇÃO
# ============================================================

def criar_grafico_evolucao(
    dados,
    unidade
):

    unidade_exibicao = (
        nome_unidade_exibicao(unidade)
    )

    dados_grafico = (
        dados[
            dados["Unidade"] == unidade
        ]
        .groupby(
            [
                "Ano",
                "Pais_Regiao"
            ],
            as_index=False
        )["Valor"]
        .mean()
        .sort_values("Ano")
    )

    figura = px.line(
        dados_grafico,
        x="Ano",
        y="Valor",
        color="Pais_Regiao",
        markers=True,
        color_discrete_sequence=PALETA,
        labels={
            "Ano": "Ano",
            "Valor": unidade_exibicao,
            "Pais_Regiao": "País / Região",
        },
    )

    figura.update_traces(
        line=dict(
            width=2.5
        ),
        marker=dict(
            size=7
        ),
    )

    figura.update_layout(
        height=350,
        hovermode="x unified",
        legend_title_text="",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.18,
            xanchor="center",
            x=0.5,
        ),
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=55
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            color="#36594B"
        ),
    )

    figura.update_xaxes(
        dtick=1,
        tickformat="d",
        gridcolor="#EDF1EF",
        linecolor="#DCE5E1",
        title=None,
    )

    figura.update_yaxes(
        gridcolor="#EDF1EF",
        linecolor="#DCE5E1",
        zeroline=False,
    )

    return figura


# ============================================================
# GRÁFICO DE COMPARAÇÃO
# ============================================================

def criar_grafico_comparativo(
    dados,
    unidade,
    ano
):

    unidade_exibicao = (
        nome_unidade_exibicao(unidade)
    )

    dados_grafico = (
        dados[
            (dados["Unidade"] == unidade)
            &
            (dados["Ano"] == ano)
        ]
        .groupby(
            "Pais_Regiao",
            as_index=False
        )["Valor"]
        .mean()
        .sort_values("Valor")
    )

    altura = max(
        300,
        min(
            380,
            180 + len(dados_grafico) * 30
        )
    )

    figura = px.bar(
        dados_grafico,
        x="Valor",
        y="Pais_Regiao",
        orientation="h",
        text="Valor",
        color="Pais_Regiao",
        color_discrete_sequence=PALETA,
        labels={
            "Valor": unidade_exibicao,
            "Pais_Regiao": "",
        },
    )

    figura.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "%{y}<br>"
            "Valor: %{x:.2f}"
            "<extra></extra>"
        ),
    )

    figura.update_layout(
        height=altura,
        showlegend=False,
        margin=dict(
            l=20,
            r=50,
            t=20,
            b=40
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            color="#36594B"
        ),
    )

    figura.update_xaxes(
        gridcolor="#EDF1EF",
        linecolor="#DCE5E1",
        zeroline=False,
    )

    figura.update_yaxes(
        title=None,
    )

    return figura


# ============================================================
# CARREGAMENTO DA BASE
# ============================================================

try:

    df = carregar_dados(
        DATA_FILE
    )

except FileNotFoundError:

    st.error(
        "Não foi possível encontrar o arquivo CSV."
    )

    st.code(
        "Custo_Dieta_Saudavel_Traduzido_Completo.csv"
    )

    st.stop()

except (
    pd.errors.ParserError,
    UnicodeDecodeError,
    ValueError,
) as erro:

    st.error(
        f"Não foi possível carregar a base: {erro}"
    )

    st.stop()


# ============================================================
# INDICADORES
# ============================================================

indicadores = sorted(
    df["Item_Analise"]
    .dropna()
    .unique()
)

indicador_padrao = (
    "Custo de uma dieta saudável (CoHD)"
)

if indicador_padrao in indicadores:

    indice_padrao = indicadores.index(
        indicador_padrao
    )

else:

    indice_padrao = 0


# ============================================================
# SIDEBAR — IDENTIDADE
# ============================================================

with st.sidebar:

    st.markdown(
    """
<div class="sidebar-brand">
    <div class="sidebar-brand-title">🌿 Custo de uma<br>Dieta Saudável</div>
    <div class="sidebar-brand-text">
        Exploração interativa de indicadores de custo e acessibilidade
        de uma dieta saudável em diferentes países e regiões.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

    st.divider()

    st.subheader(
        "🔎 Filtros"
    )


    # --------------------------------------------------------
    # INDICADOR
    # --------------------------------------------------------

    indicador = st.selectbox(
        "Indicador",
        indicadores,
        index=indice_padrao,
    )


    base_indicador = df[
        df["Item_Analise"] == indicador
    ].copy()


    # --------------------------------------------------------
    # PAÍSES
    # --------------------------------------------------------

    paises_disponiveis = sorted(
        base_indicador[
            "Pais_Regiao"
        ]
        .dropna()
        .unique()
    )


    selecao_padrao = [
        pais
        for pais in [
            "Brazil",
            "World"
        ]
        if pais in paises_disponiveis
    ]


    if (
        not selecao_padrao
        and paises_disponiveis
    ):

        selecao_padrao = [
            paises_disponiveis[0]
        ]


    paises = st.multiselect(
        "Países ou regiões",
        paises_disponiveis,
        default=selecao_padrao,
        max_selections=8,
        placeholder="Selecione até 8 opções",
    )


    st.caption(
        "Selecione até 8 países ou regiões."
    )


    # --------------------------------------------------------
    # PERÍODO
    # --------------------------------------------------------

    ano_minimo = int(
        base_indicador["Ano"].min()
    )

    ano_maximo = int(
        base_indicador["Ano"].max()
    )


    if ano_minimo == ano_maximo:

        st.info(
            f"Dados disponíveis apenas para {ano_minimo}."
        )

        periodo = (
            ano_minimo,
            ano_maximo
        )

    else:

        periodo = st.slider(
            "Período",
            min_value=ano_minimo,
            max_value=ano_maximo,
            value=(
                ano_minimo,
                ano_maximo
            ),
        )


    st.caption(
        f"Período disponível: "
        f"{ano_minimo} – {ano_maximo}"
    )


    # --------------------------------------------------------
    # SOBRE
    # --------------------------------------------------------

    st.markdown(
    """
<div class="sobre-projeto">
    <strong>ⓘ &nbsp; Sobre o projeto</strong><br><br>
    Dados sobre o custo e a acessibilidade de uma dieta saudável
    em diferentes países e regiões.<br><br>
    <strong>Fonte:</strong> FAO
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# VALIDAÇÃO DOS PAÍSES
# ============================================================

if not paises:

    st.info(
        "Selecione pelo menos um país ou região "
        "para iniciar a análise."
    )

    st.stop()


# ============================================================
# FILTRO PRINCIPAL
# ============================================================

filtrado = base_indicador[
    base_indicador[
        "Pais_Regiao"
    ].isin(paises)
    &
    base_indicador[
        "Ano"
    ].between(
        periodo[0],
        periodo[1]
    )
].copy()


filtrado = filtrado.dropna(
    subset=["Valor"]
)


if filtrado.empty:

    st.warning(
        "Não existem dados disponíveis "
        "para a seleção atual."
    )

    st.stop()


# ============================================================
# UNIDADES
# ============================================================

unidades = (
    filtrado[
        "Unidade"
    ]
    .dropna()
    .unique()
    .tolist()
)


if not unidades:

    st.warning(
        "Não foi possível identificar "
        "a unidade deste indicador."
    )

    st.stop()


# ============================================================
# CABEÇALHO
# ============================================================

cab1, cab2 = st.columns(
    [5, 1]
)


with cab1:

    st.title(
        "🥗 Custo de uma Dieta Saudável"
    )

    st.markdown(
        """
        Explore a evolução dos indicadores de
        **custo e acessibilidade de uma dieta saudável**
        em diferentes países e regiões.
        """
    )


with cab2:

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:58px;
            padding-top:5px;
        ">
            🥬
        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# DADOS DE APOIO
# ============================================================

ultimo_ano = int(
    filtrado["Ano"].max()
)

dados_ultimo_ano = filtrado[
    filtrado["Ano"] == ultimo_ano
].copy()


unidade_principal = unidades[0]

unidade_exibicao = (
    nome_unidade_exibicao(
        unidade_principal
    )
)


dados_ultimo_ano_unidade = (
    dados_ultimo_ano[
        dados_ultimo_ano["Unidade"]
        == unidade_principal
    ]
)


media_atual = (
    dados_ultimo_ano_unidade[
        "Valor"
    ].mean()
)


anos_unidade = sorted(
    filtrado[
        filtrado["Unidade"]
        == unidade_principal
    ]["Ano"]
    .dropna()
    .unique()
)


if len(anos_unidade) >= 2:

    ano_anterior = int(
        anos_unidade[-2]
    )

    media_anterior = (
        filtrado[
            (
                filtrado["Ano"]
                == ano_anterior
            )
            &
            (
                filtrado["Unidade"]
                == unidade_principal
            )
        ]["Valor"]
        .mean()
    )

else:

    ano_anterior = None
    media_anterior = None


variacao = (
    calcular_variacao_percentual(
        media_atual,
        media_anterior
    )
)


if variacao is not None:

    delta_media = (
        f"{variacao:+.1f}%"
        .replace(".", ",")
    )

else:

    delta_media = None


# ============================================================
# ABAS
# ============================================================

tab1, tab2, tab3 = st.tabs(
    [
        "▥  Visão Geral",
        "⌁  Gráficos",
        "▦  Dados",
    ]
)


# ============================================================
# ABA 1 — VISÃO GERAL
# ============================================================

with tab1:

    st.subheader(
        "Resumo da análise"
    )


    # --------------------------------------------------------
    # KPIs
    # --------------------------------------------------------

    kpi1, kpi2, kpi3, kpi4 = (
        st.columns(4)
    )


    kpi1.metric(
        "📅 Ano de referência",
        ultimo_ano
    )


    kpi2.metric(
        "👥 Países / regiões",
        len(paises)
    )


    kpi3.metric(
        "▤ Registros analisados",
        len(filtrado)
    )


    if len(unidades) == 1:

        kpi4.metric(
            f"💰 Média em {ultimo_ano}",
            formatar_valor(
                media_atual,
                unidade_principal
            ),
            delta=delta_media,
            help=(
                f"Comparação com "
                f"{ano_anterior}. "
                if ano_anterior is not None
                else
                "Não há ano anterior para comparação."
            ),
        )

    else:

        kpi4.metric(
            "📊 Unidades encontradas",
            len(unidades)
        )


    # --------------------------------------------------------
    # CONTEXTO
    # --------------------------------------------------------

    st.markdown(
    f"""
<div class="contexto-analise">
    <strong>ⓘ &nbsp; Indicador:</strong> {indicador}
    &nbsp;&nbsp; | &nbsp;&nbsp;
    <strong>Países / regiões:</strong> {", ".join(paises)}
    &nbsp;&nbsp; | &nbsp;&nbsp;
    <strong>Período:</strong> {periodo[0]} – {periodo[1]}
    <br>
    <strong>Unidade:</strong> {" • ".join(nome_unidade_exibicao(u) for u in unidades)}
</div>
""",
    unsafe_allow_html=True,
)


    # --------------------------------------------------------
    # GRÁFICOS LADO A LADO
    # --------------------------------------------------------

    unidade = unidades[0]

    st.markdown(
        f"### {nome_unidade_exibicao(unidade)}"
    )


    graf1, graf2 = st.columns(
        [1.2, 0.8],
        gap="medium"
    )


    with graf1:

        st.markdown(
            "#### 📈 Evolução ao longo do tempo"
        )

        figura_evolucao = (
            criar_grafico_evolucao(
                filtrado,
                unidade
            )
        )

        st.plotly_chart(
            figura_evolucao,
            use_container_width=True,
            key="visao_evolucao_0",
            config={
                "displaylogo": False,
                "responsive": True,
            },
        )


    with graf2:

        st.markdown(
            f"#### ▥ Comparação — {ultimo_ano}"
        )

        dados_comparacao = filtrado[
            (
                filtrado["Unidade"]
                == unidade
            )
            &
            (
                filtrado["Ano"]
                == ultimo_ano
            )
        ]


        if not dados_comparacao.empty:

            figura_comparacao = (
                criar_grafico_comparativo(
                    filtrado,
                    unidade,
                    ultimo_ano,
                )
            )

            st.plotly_chart(
                figura_comparacao,
                use_container_width=True,
                key="visao_comparacao_0",
                config={
                    "displaylogo": False,
                    "responsive": True,
                },
            )

        else:

            st.info(
                "Não existem dados para comparação "
                f"em {ultimo_ano}."
            )


    # --------------------------------------------------------
    # SEGUNDA UNIDADE, SE EXISTIR
    # --------------------------------------------------------

    if len(unidades) >= 2:

        st.divider()

        unidade = unidades[1]

        st.markdown(
            f"### {nome_unidade_exibicao(unidade)}"
        )


        graf3, graf4 = st.columns(
            [1.2, 0.8],
            gap="medium"
        )


        with graf3:

            st.markdown(
                "#### 📈 Evolução ao longo do tempo"
            )

            figura_evolucao_2 = (
                criar_grafico_evolucao(
                    filtrado,
                    unidade
                )
            )

            st.plotly_chart(
                figura_evolucao_2,
                use_container_width=True,
                key="visao_evolucao_1",
                config={
                    "displaylogo": False
                },
            )


        with graf4:

            st.markdown(
                f"#### ▥ Comparação — {ultimo_ano}"
            )

            dados_comparacao_2 = filtrado[
                (
                    filtrado["Unidade"]
                    == unidade
                )
                &
                (
                    filtrado["Ano"]
                    == ultimo_ano
                )
            ]


            if not dados_comparacao_2.empty:

                figura_comparacao_2 = (
                    criar_grafico_comparativo(
                        filtrado,
                        unidade,
                        ultimo_ano,
                    )
                )

                st.plotly_chart(
                    figura_comparacao_2,
                    use_container_width=True,
                    key="visao_comparacao_1",
                    config={
                        "displaylogo": False
                    },
                )

            else:

                st.info(
                    "Não existem dados para comparação "
                    f"em {ultimo_ano}."
                )


    if len(unidades) > 2:

        st.info(
            "O indicador possui mais de duas unidades. "
            "As duas primeiras foram exibidas para manter "
            "a leitura do dashboard organizada."
        )


# ============================================================
# ABA 2 — GRÁFICOS
# ============================================================

with tab2:

    st.subheader(
        "Análise gráfica"
    )

    st.caption(
        "Visualize separadamente a evolução e a "
        "comparação dos países ou regiões selecionados."
    )


    for indice, unidade in enumerate(
        unidades[:2]
    ):

        unidade_exibicao_loop = (
            nome_unidade_exibicao(
                unidade
            )
        )


        st.markdown(
            f"### {unidade_exibicao_loop}"
        )


        st.markdown(
            "#### Evolução temporal"
        )


        figura = (
            criar_grafico_evolucao(
                filtrado,
                unidade
            )
        )


        st.plotly_chart(
            figura,
            use_container_width=True,
            key=f"grafico_evolucao_{indice}",
            config={
                "displaylogo": False
            },
        )


        st.markdown(
            f"#### Comparação entre países — "
            f"{ultimo_ano}"
        )


        dados_comp = filtrado[
            (
                filtrado["Unidade"]
                == unidade
            )
            &
            (
                filtrado["Ano"]
                == ultimo_ano
            )
        ]


        if not dados_comp.empty:

            figura_comp = (
                criar_grafico_comparativo(
                    filtrado,
                    unidade,
                    ultimo_ano
                )
            )


            st.plotly_chart(
                figura_comp,
                use_container_width=True,
                key=f"grafico_comparacao_{indice}",
                config={
                    "displaylogo": False
                },
            )


        if indice < min(
            len(unidades),
            2
        ) - 1:

            st.divider()


# ============================================================
# ABA 3 — DADOS
# ============================================================

with tab3:

    cab_tabela, cab_download = (
        st.columns(
            [3, 1]
        )
    )


    with cab_tabela:

        st.subheader(
            "Dados utilizados na análise"
        )

        st.caption(
            "Registros correspondentes aos "
            "filtros atualmente selecionados."
        )


    # --------------------------------------------------------
    # TABELA
    # --------------------------------------------------------

    tabela = filtrado[
        [
            "Pais_Regiao",
            "Ano",
            "Unidade",
            "Valor",
            "Status_Dado",
        ]
    ].copy()


    tabela["Unidade"] = (
        tabela["Unidade"]
        .map(
            nome_unidade_exibicao
        )
    )


    tabela = tabela.rename(
        columns={
            "Pais_Regiao":
                "País / Região",

            "Status_Dado":
                "Status",
        }
    )


    tabela = tabela.sort_values(
        [
            "País / Região",
            "Ano",
            "Unidade",
        ]
    )


    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    csv_download = (
        tabela
        .to_csv(
            index=False
        )
        .encode(
            "utf-8-sig"
        )
    )


    with cab_download:

        st.write("")

        st.download_button(
            label="⬇ Baixar dados filtrados",
            data=csv_download,
            file_name=(
                "dados_dieta_filtrados.csv"
            ),
            mime="text/csv",
            use_container_width=True,
        )


    st.dataframe(
        tabela,
        use_container_width=True,
        hide_index=True,
        column_config={

            "Ano":
                st.column_config.NumberColumn(
                    "Ano",
                    format="%d",
                ),

            "Valor":
                st.column_config.NumberColumn(
                    "Valor",
                    format="%.2f",
                ),
        },
    )


# ============================================================
# INFORMAÇÕES DA BASE
# ============================================================

st.write("")

with st.expander(
    "📚 Fonte e informações sobre os dados"
):

    info1, info2, info3, info4 = (
        st.columns(4)
    )


    info1.metric(
        "Registros",
        f"{len(df):,.0f}"
        .replace(",", ".")
    )


    info2.metric(
        "Países / regiões",
        df[
            "Pais_Regiao"
        ].nunique()
    )


    info3.metric(
        "Ano inicial",
        int(
            df["Ano"].min()
        )
    )


    info4.metric(
        "Ano final",
        int(
            df["Ano"].max()
        )
    )


    st.divider()


    info5, info6 = st.columns(2)


    with info5:

        st.write(
            "**Indicadores disponíveis:**",
            df[
                "Item_Analise"
            ].nunique()
        )


    with info6:

        st.write(
            "**Unidades disponíveis:**",
            df[
                "Unidade"
            ].nunique()
        )


    if not df[
        "Publicacao"
    ].dropna().empty:

        st.write(
            "**Publicação:**",
            df[
                "Publicacao"
            ]
            .dropna()
            .iloc[0]
        )


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.markdown(
    """
    <div class="rodape">

        🥗 Custo de uma Dieta Saudável
        &nbsp; • &nbsp;
        Python + Pandas + Plotly + Streamlit

    </div>
    """,
    unsafe_allow_html=True,
)