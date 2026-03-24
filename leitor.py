import pandas as pd

def ler_planilha(caminho):
    """
    Lê um arquivo Excel ou CSV e retorna um resumo dos dados.
    caminho → é o caminho do arquivo que o usuário selecionou
    """

    # Detecta o tipo do arquivo pelo final do nome
    if caminho.endswith(".csv"):
        df = pd.read_csv(caminho)
    else:
        df = pd.read_excel(caminho)

    # ── Informações gerais ─────────────────────────
    total_linhas, total_colunas = df.shape  # shape retorna (linhas, colunas)
    nomes_colunas = list(df.columns)        # lista com o nome de cada coluna

    # ── Resumo estatístico só das colunas numéricas ─
    colunas_numericas = df.select_dtypes(include="number")

    resumo_estatistico = {}
    for coluna in colunas_numericas.columns:
        resumo_estatistico[coluna] = {
            "média": round(float(df[coluna].mean()), 2),
            "mínimo": round(float(df[coluna].min()), 2),
            "máximo": round(float(df[coluna].max()), 2),
            "total": round(float(df[coluna].sum()), 2),
        }

    # ── Primeiras 5 linhas da tabela ───────────────
    amostra = df.head(5).to_string(index=False)

    # ── Monta o resultado final ────────────────────
    resultado = {
        "total_linhas":        total_linhas,
        "total_colunas":       total_colunas,
        "colunas":             nomes_colunas,
        "resumo_estatistico":  resumo_estatistico,
        "amostra":             amostra,
    }

    return resultado