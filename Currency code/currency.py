# Imports
import tkinter as tk
import requests
from PIL import Image, ImageTk

# Função para converter
def converter():
    try:
        # DOLAR
        valor_em_real = float(entrada.get())
        resposta_USD = requests.get(
            "https://economia.awesomeapi.com.br/json/last/BRL-USD")
        dados_USD = resposta_USD.json()
        cotacao_USD = float(dados_USD["BRLUSD"]["bid"])
        valor_em_dolar = valor_em_real * cotacao_USD
        resultado_USD["text"] = f"O valor em dolar é: R${valor_em_dolar:.2f}"
        # EURO
        resposta_EUR = requests.get(
            "https://economia.awesomeapi.com.br/json/last/BRL-EUR")
        dados_EUR = resposta_EUR.json()
        cotacao_EUR = float(dados_EUR["BRLEUR"]["bid"])
        valor_em_euro = valor_em_real * cotacao_EUR
        resultado_EUR["text"] = f"O valor em euro é: R${valor_em_euro:.2f}"
        # LIBRA ESTERLINA
        resposta_GBP = requests.get(
            "https://economia.awesomeapi.com.br/json/last/BRL-GBP")
        dados_GBP = resposta_GBP.json()
        cotacao_GBP = float(dados_GBP["BRLGBP"]["bid"])
        valor_em_libra_esterlina = valor_em_real * cotacao_GBP
        resultado_GBP["text"] = f"O valor em libra esterlina é: R${valor_em_libra_esterlina:.2f}"
    except:
        resultado_USD["text"] = "Error: Falha na conexão"


# Criando a janela
janela = tk.Tk()
janela.configure(bg="#1f1f24")
janela.title("Conversor de moedas")
janela.geometry("400x500")

# Carregando e ajustando o ícone do título
imagem_original = Image.open("currency.png")
imagem_redimensionada = imagem_original.resize((50, 50))
icone_titulo = ImageTk.PhotoImage(imagem_redimensionada)

# Criando um frame para o título
topo = tk.Frame(janela, bg="#1f1f24")
topo.pack(pady=10)

# Título
titulo = tk.Label(topo, text='''Currency Converter
  =-=-=-=-=-=-=-=-=-= 
   |  BRL -> USD  |    
   |  BRL -> EUR  |    
   |  BRL -> GBP  |    
  =-=-=-=-=-=-=-=-=-=  ''', bg=("#1f1f24"), fg="#fa3131", font=("Arial", 18), image=icone_titulo, compound="top")
titulo.pack()

# Carregando a imagem na mémoria
titulo.imagem = icone_titulo
titulo.pack()

# Criando um frame central
frame_central = tk.Frame(janela, bg="#1f1f24")
frame_central.pack(expand=True)

# Texto em cima do entry
texto_explicativo = tk.Label(
    frame_central,
    text="Digite um valor em BRL para converte-lo em:",
    bg="#1f1f24",
    fg="#F15050",
    font=("Arial", 12, "bold")
)
texto_explicativo.pack()

texto_explicativo2 = tk.Label(
    frame_central,
    text="USD | EUR | GBP ",
    bg="#1f1f24",
    fg="#9bf6ff",
    font=("Arial", 12)
)
texto_explicativo2.pack(pady=(0, 10))

# O ''input'' do valor em BRL
entrada = tk.Entry(frame_central, font=("Arial", 14), justify="center")
entrada.pack(pady=10)

# Botão de converter
botao = tk.Button(frame_central, text="CONVERTER", bg=(
    "#bdb2ff"), command=converter, font=("Arial", 10, "bold"))
botao.pack()

# resultado DOLAR
resultado_USD = tk.Label(frame_central, text="", bg=(
    "#1f1f24"), fg=("#9bf6ff"), font=("Arial", 12))
resultado_USD.pack(pady=5)

# resultado EURO
resultado_EUR = tk.Label(frame_central, text="", bg=(
    "#1f1f24"), fg=("#9bf6ff"), font=("Arial", 12))
resultado_EUR.pack(pady=5)

# resultado LIBRA ESTERLINA
resultado_GBP = tk.Label(frame_central, text="", bg=(
    "#1f1f24"), fg=("#9bf6ff"), font=("Arial", 12))
resultado_GBP.pack(pady=5)

# Rodar a janela
janela.mainloop()
