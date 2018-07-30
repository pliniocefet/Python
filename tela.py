# encoding: utf-8
from tkinter import *

# Variaveis globais podem ser usadas em qualquer parte do modulo
global blue 
blue = False

global red
red = False

global green
green = False

def comando(opcao):
    global blue
    global red
    global green
    
    if (opcao == 1 and blue == False):
        print("Liga led azul")
        blue = True
        
    elif (opcao == 1 and blue == True):
        print("Desliga led azul")
        blue = False
        
    elif (opcao == 2 and red == False):
        print("Liga led vermelho")
        red = True
        
    elif (opcao == 2 and red == True):
        print("Desliga led vermelho")
        red = False
        
    elif (opcao == 3 and green == False):
        print("Liga led verde")
        green = True
        
    elif (opcao == 3 and green == True):
        print("Desliga led verde")
        green = False

janela = Tk()
janela.title("Tela Principal")
janela.geometry("750x750")

texto_blue = Label(text="led azul", fg= "blue")
texto_blue.place(x=60, y=60)

texto_red = Label(text="led vermelho", fg= "red")
texto_red.place(x=150, y=60)

texto_green = Label(text="led verde", fg= "green")
texto_green.place(x=270, y=60)

# Se colocar os parentes da função Python chama a função sozinho.
# Se não colocar usuario chama a função clicando no botão
# o comando lambda não sei o que faz
botao_blue = Button(text="pisca led azul", command= lambda: comando(1), bg= "blue", fg= "white") 
botao_blue.place(x=60, y=80)

botao_red = Button(text="pisca led vermelho", command= lambda: comando(2), bg= "red", fg= "white") 
botao_red.place(x=150, y=80)

botao_green = Button(text="pisca led verde", command= lambda: comando(3), bg= "green", fg= "white") 
botao_green.place(x=270, y=80)

janela.mainloop()