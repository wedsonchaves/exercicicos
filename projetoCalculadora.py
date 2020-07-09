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
rotulo = tkinter.Label(janela, text="CALCULADORA ")
rotulo.pack()

#criando um campo de texto
campoNome = tkinter.Entry(janela)
campoNome.pack()

#evento -> uma funcao q é executada com uma acao do usuario na GUI

def clicou():
    tkinter.messagebox.showinfo("Mensagem", "Bem vindo, " + campoNome.get())

# criando um botao
botao = tkinter.Button(janela, text="1", command=clicou)
botao.place(x=50, y=90)




# 4ª Etapa - Manter o programa ativo (Front - GUI e Back - Código Python em si)
janela.mainloop()
