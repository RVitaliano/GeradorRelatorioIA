import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import os
from leitor import ler_planilha
from analisador import analisar_dados
from gerador import gerar_relatorio

# ── Configurações visuais ──────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── Variável global do arquivo ─────────────────────
arquivo_selecionado = ""

# ── Função de upload ───────────────────────────────
def selecionar_arquivo():
    global arquivo_selecionado

    caminho = filedialog.askopenfilename(
        title="Selecione a planilha",
        filetypes=[("Arquivos Excel e CSV", "*.xlsx *.xls *.csv")]
    )

    if caminho:
        arquivo_selecionado = caminho
        nome_arquivo = caminho.split("/")[-1]
        label_arquivo.configure(text=f"✅ {nome_arquivo}")
    else:
        label_arquivo.configure(text="Nenhum arquivo selecionado")

# ── Função principal ───────────────────────────────
def gerar():
    if not arquivo_selecionado:
        label_status.configure(text="⚠️ Selecione uma planilha primeiro!", text_color="orange")
        return

    tipo   = dropdown_tipo.get()
    idioma = dropdown_idioma.get()

    # ── Abre janela pra escolher onde salvar ──────
    caminho_saida = filedialog.asksaveasfilename(
        title="Salvar relatório como...",
        defaultextension=".docx",
        initialfile=f"relatorio_{tipo.lower()}.docx",
        filetypes=[("Documento Word", "*.docx")]
    )

    # Se o usuário cancelou a janela de salvar
    if not caminho_saida:
        label_status.configure(text="⚠️ Operação cancelada.", text_color="orange")
        return

    # Desativa o botão pra não clicar duas vezes
    btn_gerar.configure(state="disabled", text="⏳ Gerando...")
    label_status.configure(text="📊 Iniciando...", text_color="white")

    # Roda em thread separada pra não travar a janela
    threading.Thread(target=processar, args=(caminho_saida,)).start()

def processar(caminho_saida):
    try:
        tipo   = dropdown_tipo.get()
        idioma = dropdown_idioma.get()
        obs    = caixa_obs.get("1.0", "end").strip()

        # Etapa 1 — lê a planilha
        atualizar_status("📊 Lendo planilha...")
        dados = ler_planilha(arquivo_selecionado)

        # Etapa 2 — chama a IA
        atualizar_status("🤖 Analisando com IA (pode demorar um pouco)...")
        analise = analisar_dados(dados, tipo, idioma, obs)

        # Etapa 3 — gera o .docx
        atualizar_status("📝 Gerando relatório Word...")
        caminho = gerar_relatorio(analise, dados, tipo, caminho_saida)

        # Sucesso!
        atualizar_status(f"✅ Salvo em: {caminho}", cor="lightgreen")
        btn_gerar.configure(state="normal", text="🚀 Gerar Relatório")

        # Pergunta se quer abrir o arquivo
        if messagebox.askyesno("Concluído!", "Relatório gerado com sucesso!\nDeseja abrir o arquivo agora?"):
            os.startfile(caminho)

    except Exception as e:
        atualizar_status(f"❌ Erro: {str(e)}", cor="red")
        btn_gerar.configure(state="normal", text="🚀 Gerar Relatório")

def atualizar_status(texto, cor="white"):
    label_status.configure(text=texto, text_color=cor)

# ── Janela principal ───────────────────────────────
janela = ctk.CTk()
janela.title("Gerador de Relatórios IA")
janela.geometry("500x620")

# ── Título ─────────────────────────────────────────
titulo = ctk.CTkLabel(
    janela,
    text="📊 Gerador de Relatórios IA",
    font=ctk.CTkFont(size=20, weight="bold")
)
titulo.pack(pady=20)

# ── Botão de upload ────────────────────────────────
btn_upload = ctk.CTkButton(
    janela,
    text="📁 Selecionar Planilha (Excel ou CSV)",
    command=selecionar_arquivo
)
btn_upload.pack(pady=10)

label_arquivo = ctk.CTkLabel(janela, text="Nenhum arquivo selecionado")
label_arquivo.pack(pady=5)

# ── Dropdown: tipo de relatório ────────────────────
label_tipo = ctk.CTkLabel(janela, text="Tipo de Relatório:")
label_tipo.pack(pady=(15, 0))

dropdown_tipo = ctk.CTkOptionMenu(
    janela,
    values=["Vendas", "Financeiro", "RH", "Estoque", "Marketing"]
)
dropdown_tipo.pack(pady=5)

# ── Dropdown: idioma ───────────────────────────────
label_idioma = ctk.CTkLabel(janela, text="Idioma do Relatório:")
label_idioma.pack(pady=(15, 0))

dropdown_idioma = ctk.CTkOptionMenu(
    janela,
    values=["Português", "Inglês", "Espanhol"]
)
dropdown_idioma.pack(pady=5)

# ── Caixa de observações ───────────────────────────
label_obs = ctk.CTkLabel(janela, text="Observações para a IA (opcional):")
label_obs.pack(pady=(15, 0))

caixa_obs = ctk.CTkTextbox(janela, height=100, width=400)
caixa_obs.pack(pady=5)

# ── Botão gerar ────────────────────────────────────
btn_gerar = ctk.CTkButton(
    janela,
    text="🚀 Gerar Relatório",
    fg_color="green",
    hover_color="darkgreen",
    command=gerar
)
btn_gerar.pack(pady=20)

# ── Status ─────────────────────────────────────────
label_status = ctk.CTkLabel(janela, text="")
label_status.pack(pady=5)

# ── Inicia ─────────────────────────────────────────
janela.mainloop()