# 1ª Etapa - Importar a biblioteca TKinter (GUI)
import tkinter
import tkinter.messagebox


# 2ª Etapa - Criar a janela principal da minha GUI (Widget)
janela = tkinter.Tk()

# 3ª Etapa - Customizações na minha Janela Principal
janela.title("CALCULADORA")
janela.geometry("250x350")

# Etapa - 3.1 - Inserir outros widgets (Rótulos, botões, caixas de texto, etc)
# variavel = tekinter.<Funcao de criacao>


#criando um campo de texto
campoNome = tkinter.Entry(janela)
campoNome.pack()

#evento -> uma funcao q é executada com uma acao do usuario na GUI
num1 = 0
num2 = 0
def resultado():
    tkinter.messagebox.showinfo("Resultado", "O resultado é, " + str(num1))

# criando um botao

#1

botao = tkinter.Button(janela, text="AC")
botao.place(x=45, y=90)
botao = tkinter.Button(janela, text="+/-")
botao.place(x=90, y=90)
botao = tkinter.Button(janela, text="%")
botao.place(x=135, y=90)
botao = tkinter.Button(janela, text="/")
botao.place(x=180, y=90)

#2

botao = tkinter.Button(janela, text="7")
botao.place(x=45, y=135)
botao = tkinter.Button(janela, text="8")
botao.place(x=90, y=135)
botao = tkinter.Button(janela, text="9")
botao.place(x=135, y=135)
botao = tkinter.Button(janela, text="x")
botao.place(x=180, y=135)

#3

botao = tkinter.Button(janela, text="4")
botao.place(x=45, y=180)
botao = tkinter.Button(janela, text="5")
botao.place(x=90, y=180)
botao = tkinter.Button(janela, text="6")
botao.place(x=135, y=180)
botao = tkinter.Button(janela, text="-")
botao.place(x=180, y=180)

#4

botao = tkinter.Button(janela, text="1")
botao.place(x=45, y=225)
botao = tkinter.Button(janela, text="2")
botao.place(x=90, y=225)
botao = tkinter.Button(janela, text="3")
botao.place(x=135, y=225)
botao = tkinter.Button(janela, text="+")
botao.place(x=180, y=225)

#5

botao = tkinter.Button(janela, text="0           ")
botao.place(x=45, y=270)

botao = tkinter.Button(janela, text=".")
botao.place(x=135, y=270)
botaoResultado = tkinter.Button(janela, text="=", command=resultado)
botaoResultado.place(x=180, y=270)


# 4ª Etapa - Manter o programa ativo (Front - GUI e Back - Código Python em si)
janela.mainloop()
