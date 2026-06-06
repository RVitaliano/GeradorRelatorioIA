import pandas as pd

def ler_planilha(caminho):
    if caminho.endswith(".csv"):
        df = pd.read_csv(caminho)
    else:
        df = pd.read_excel(caminho)

    total_linhas, total_colunas = df.shape
    nomes_colunas = list(df.columns)

    colunas_numericas = df.select_dtypes(include="number")

    resumo_estatistico = {}
    for coluna in colunas_numericas.columns:
        resumo_estatistico[coluna] = {
            "mean": round(float(df[coluna].mean()), 2),
            "min":  round(float(df[coluna].min()), 2),
            "max":  round(float(df[coluna].max()), 2),
            "sum":  round(float(df[coluna].sum()), 2),
        }

    amostra = df.head(20).to_string(index=False)

    resultado = {
        "total_linhas":       total_linhas,
        "total_colunas":      total_colunas,
        "colunas":            nomes_colunas,
        "resumo_estatistico": resumo_estatistico,
        "amostra":            amostra,
    }

    return resultado