from groq import Groq

def analisar_dados(dados, tipo_relatorio, idioma, observacoes=""):

    contexto = f"""
Você é um analista de dados profissional. Analise os dados abaixo e gere um relatório completo em {idioma}.

TIPO DE RELATÓRIO: {tipo_relatorio}

INFORMAÇÕES DA PLANILHA:
- Total de registros: {dados['total_linhas']}
- Colunas disponíveis: {', '.join(dados['colunas'])}

RESUMO ESTATÍSTICO:
"""

    for coluna, stats in dados["resumo_estatistico"].items():
        contexto += f"- {coluna}: média={stats['média']}, mínimo={stats['mínimo']}, máximo={stats['máximo']}, total={stats['total']}\n"

    contexto += f"""
AMOSTRA DOS DADOS (primeiras 5 linhas):
{dados['amostra']}
"""

    if observacoes:
        contexto += f"\nOBSERVAÇÕES ADICIONAIS DO USUÁRIO:\n{observacoes}\n"

    contexto += """
Gere um relatório profissional com:
1. Resumo executivo
2. Principais insights dos dados
3. Pontos de atenção
4. Recomendações

Use linguagem clara e profissional.
"""

    cliente = Groq(api_key="SUA_CHAVE_GROQ_AQUI")

    resposta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": contexto}
        ]
    )

    return resposta.choices[0].message.content