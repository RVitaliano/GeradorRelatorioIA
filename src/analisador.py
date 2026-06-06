import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def analisar_dados(dados, tipo_relatorio, idioma, observacoes=""):

    contexto = f"""
REPORT TYPE: {tipo_relatorio}

SPREADSHEET INFORMATION:
- Total records: {dados['total_linhas']}
- Available columns: {', '.join(dados['colunas'])}

STATISTICAL SUMMARY:
"""

    for coluna, stats in dados["resumo_estatistico"].items():
        contexto += f"- {coluna}: mean={stats['mean']}, min={stats['min']}, max={stats['max']}, sum={stats['sum']}\n"

    contexto += f"""
DATA SAMPLE (first 20 rows):
{dados['amostra']}
"""

    if observacoes:
        contexto += f"\nADDITIONAL USER NOTES:\n{observacoes}\n"

    estrutura = {
        "Português": """
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
""",
        "Inglês": """
Generate a professional and detailed report with exactly this structure:

1. Executive Summary
   - Overview of the data in 2-3 paragraphs
   - Key numbers and highlights

2. Key Insights
   - List at least 5 relevant insights based on the data
   - Relate patterns, trends and comparisons between columns

3. Points of Attention
   - Identify anomalies, extreme values or concerning situations
   - Be specific with numbers

4. Recommendations
   - Suggest at least 4 concrete actions based on the data
   - Prioritize by impact

Use clear, professional and objective language.
Do not invent data that is not in the context above.
Do not use Markdown with asterisks — use only plain text and numbering.
""",
        "Espanhol": """
Genere un informe profesional y detallado con exactamente esta estructura:

1. Resumen Ejecutivo
   - Visión general de los datos en 2-3 párrafos
   - Números clave y aspectos destacados

2. Insights Principales
   - Liste al menos 5 insights relevantes basados en los datos
   - Relacione patrones, tendencias y comparaciones entre columnas

3. Puntos de Atención
   - Identifique anomalías, valores extremos o situaciones preocupantes
   - Sea específico con los números

4. Recomendaciones
   - Sugiera al menos 4 acciones concretas basadas en los datos
   - Priorice por impacto

Use lenguaje claro, profesional y objetivo.
No invente datos que no estén en el contexto anterior.
No use Markdown con asteriscos — use solo texto simple y numeración.
"""
    }

    contexto += estrutura.get(idioma, estrutura["Português"])

    cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))

    resposta = cliente.chat.completions.create(
        model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),
        messages=[
            {
                "role": "system",
                "content": f"You are a senior data analyst specialized in {tipo_relatorio} reports. Always respond in {idioma}. Be direct, precise and base your analysis only on the provided data."
            },
            {
                "role": "user",
                "content": contexto
            }
        ]
    )

    return resposta.choices[0].message.content