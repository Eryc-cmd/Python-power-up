# bibliotecas = pacotes de codigos
# pip install pyautogui

import pyautogui
import time
# pyautogui.click -> clica
# pyautogui.write -> escrever um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do programa
# Passo 1: Entrar no sistema da empresa
# abrir o navegador
pyautogui.press("win")
pyautogui.write(pythonimpressionador@gmail.com  sua senha muito muito muito dificilima  
                "chrome")
pyautogui.press("enter")
pyautogui.click(x=995, y=393)
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
#fazer uma pausa maior pro site carregar atraves da biblioteca (time)
time.sleep(3)

# Passo 2: Fazer login
#clicar no campo de email
pyautogui.click(x=478, y=377)
pyautogui.write("pythonimpressionador@gmail.com")# meu email
pyautogui.press("tab")#passar para o proximo campo
pyautogui.write("sua senha muito muito muito dificilima")#minha senha para logar
pyautogui.press("tab")
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 3: abrir a base de dados(importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")#nome do arquivo
print(tabela)

for linha in tabela.index: #para cada linha dentro da minha tabela executa o codigo (index=linha de produto)
    # passo 4: cadastrar 1 produto
    # codigo
    pyautogui.click(x=458, y=261)#clicar no campo do codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write("codigo")
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write("marca")
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write("tipo")
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write("categoria")
    pyautogui.press("tab")
    # preço
    preco = str(tabela.loc[linha, "preco"])
    pyautogui.write("preco")
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write("custo")
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.press("tab") # passar para o botao enviar

    pyautogui.press("enter") #clicou no enviar
    #str numero em texto
    #voltar para o inicio
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 ate acabar a lista de produtos
# suporte 21967218715