# 📊 Gerador Automático de Relatórios com IA

Aplicação desktop desenvolvida em Python que lê planilhas Excel ou CSV, analisa os dados automaticamente com Inteligência Artificial e gera um relatório profissional em Word (.docx) — tudo com poucos cliques.

---

## 🖥️ Interface

<img width="620" height="732" alt="image" src="https://github.com/user-attachments/assets/fcdc903b-6056-4c45-b997-203675b2eeac" />

- Seleção de planilha via explorador de arquivos
- Escolha do tipo de relatório (Vendas, RH, Financeiro, Estoque, Marketing)
- Escolha do idioma (Português, Inglês, Espanhol)
- Campo de observações personalizadas para a IA
- Escolha do nome e pasta ao salvar o relatório

---

## ⚙️ Tecnologias utilizadas

| Tecnologia | Função |
|------------|--------|
| Python 3.10+ | Linguagem principal |
| CustomTkinter | Interface gráfica desktop |
| Pandas + OpenPyXL | Leitura e processamento de planilhas |
| Groq API (LLaMA 3.3 70B) | Análise dos dados com IA |
| Python-docx | Geração do relatório Word |
| python-dotenv | Gerenciamento seguro da chave de API |
| Threading | Processamento assíncrono |

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/RVitaliano/GeradorRelatorioIA
cd GeradorRelatorioIA
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Windows (CMD)
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install customtkinter pandas openpyxl groq python-docx python-dotenv
```

### 4. Configure sua chave da API

Acesse [console.groq.com](https://console.groq.com), crie uma conta gratuita e gere uma chave de API.

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
GROQ_API_KEY=sua_chave_aqui
MODEL_NAME=llama-3.3-70b-versatile
```

> ⚠️ Nunca compartilhe ou versione o arquivo `.env`. Ele já está no `.gitignore`.

### 5. Execute o projeto

```bash
python app.py
```

---

## 📁 Estrutura do projeto

```
GeradorRelatorioIA/
│
├── app.py              # Interface gráfica principal e orquestração
├── src/
│   ├── __init__.py
│   ├── leitor.py       # Leitura e processamento da planilha
│   ├── analisador.py   # Integração com a IA (Groq API)
│   └── gerador.py      # Geração do relatório Word
│
├── .env                # Variáveis de ambiente (não versionado)
├── .env.example        # Template do .env
├── requirements.txt    # Dependências do projeto
├── .gitignore
└── README.md
```

---

## 📋 Como usar

1. Abra o programa com `python app.py`
2. Clique em **Selecionar Planilha** e escolha seu arquivo Excel ou CSV
3. Escolha o **tipo de relatório** e o **idioma**
4. Adicione **observações** opcionais para guiar a análise da IA
5. Clique em **Gerar Relatório**
6. Escolha onde salvar e aguarde — o relatório será gerado automaticamente!

---

## 📄 Estrutura do relatório gerado

O sistema gera um documento Word (.docx) com:

- Cabeçalho com título e data de geração
- Informações gerais da planilha (total de registros e colunas)
- Tabela de resumo estatístico (média, mínimo, máximo e total por coluna numérica)
- Análise completa gerada por IA com:
  - Resumo executivo
  - Principais insights
  - Pontos de atenção
  - Recomendações

---

## 📂 Formatos de entrada suportados

| Formato | Extensão |
|---------|----------|
| Excel moderno | `.xlsx` |
| Excel legado | `.xls` |
| CSV | `.csv` |

---

## ⚠️ Observações

- A chave da API Groq é **gratuita** — crie a sua em [console.groq.com](https://console.groq.com)
- O tempo de geração depende do tamanho da planilha e da velocidade da API
- O processamento roda em thread separada — a interface não trava durante a geração

---

## 👤 Autor

Desenvolvido como projeto de hiperautomação — aplicação de IA generativa integrada a um fluxo completo de leitura de dados e geração de documentos.
