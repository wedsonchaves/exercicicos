# 1ª Etapa - Importar a biblioteca TKinter (GUI)
import tkinter
import tkinter.messagebox


# 2ª Etapa - Criar a janela principal da minha GUI (Widget)
janela = tkinter.Tk()

# 3ª Etapa - Customizações na minha Janela Principal
janela.title("Programa")
janela.geometry("800x600")

# Etapa - 3.1 - Inserir outros widgets (Rótulos, botões, caixas de texto, etc)
# variavel = tekinter.<Funcao de criacao>

#criando um rotulo 
num1 = tkinter.Label(janela, text="Número 1:")
num1.pack()

campoNum1 = tkinter.Entry(janela)
campoNum1.pack()

num2 = tkinter.Label(janela, text="Número 2:")
num2.pack()

campoNum2 = tkinter.Entry(janela)
campoNum2.pack()

#evento -> uma funcao q é executada com uma acao do usuario na GUI

def calcular():
    soma = float(campoNum1.get()) + float(campoNum2.get())
    tkinter.messagebox.showinfo("Resultado:", "A soma é, " + str(soma))

# criando um botao
botao = tkinter.Button(janela, text="Calcular", command=calcular)
botao.pack()




# 4ª Etapa - Manter o programa ativo (Front - GUI e Back - Código Python em si)
janela.mainloop()
