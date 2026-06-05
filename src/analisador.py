import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def analisar_dados(dados, tipo_relatorio, idioma, observacoes=""):

    contexto = f"""
TIPO DE RELATÓRIO: {tipo_relatorio}

INFORMAÇÕES DA PLANILHA:
- Total de registros: {dados['total_linhas']}
- Colunas disponíveis: {', '.join(dados['colunas'])}

RESUMO ESTATÍSTICO:
"""

    for coluna, stats in dados["resumo_estatistico"].items():
        contexto += f"- {coluna}: média={stats['média']}, mínimo={stats['mínimo']}, máximo={stats['máximo']}, total={stats['total']}\n"

    contexto += f"""
AMOSTRA DOS DADOS (primeiras 20 linhas):
{dados['amostra']}
"""

    if observacoes:
        contexto += f"\nOBSERVAÇÕES ADICIONAIS DO USUÁRIO:\n{observacoes}\n"

    contexto += """
Gere um relatório profissional e detalhado com exatamente esta estrutura:

1. Resumo Executivo
   - Visão geral dos dados em 2-3 parágrafos
   - Principais números e destaques

2. Principais Insights
   - Liste ao menos 5 insights relevantes com base nos dados
   - Relacione padrões, tendências e comparações entre colunas

3. Pontos de Atenção
   - Identifique anomalias, valores extremos ou situações preocupantes
   - Seja específico com números

4. Recomendações
   - Sugira ao menos 4 ações concretas baseadas nos dados
   - Priorize por impacto

Use linguagem clara, profissional e objetiva.
Não invente dados que não estejam no contexto acima.
Não use Markdown com asteriscos — use apenas texto simples e numeração.
"""

    cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))

    resposta = cliente.chat.completions.create(
        model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),
        messages=[
            {
                "role": "system",
                "content": f"Você é um analista de dados sênior especializado em relatórios de {tipo_relatorio}. Responda sempre em {idioma}. Seja direto, preciso e baseie-se apenas nos dados fornecidos."
            },
            {
                "role": "user",
                "content": contexto
            }
        ]
    )

    return resposta.choices[0].message.content