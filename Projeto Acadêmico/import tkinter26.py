import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# importando bilbiotecas
from PIL import ImageTk, Image
import requests
import json

# Declaração de variáveis
global imagem, erro1, sigla_moeda

co0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#6f9fbd"  # azul
cor3  = "#000000"

l_fonte = 'Calibri'

erro1 = 0
sigla_moeda = 'USD'

lista_moeda = [    
        'USD',
        'EUR',
        'GBP',
        'ARS',
        'JPY',
        'BOB',
        'CLP',
        'COP' 
]

fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

# Funções
def info():
    moeda1_x = caixa_combo_moeda1.get()
    moeda_api = moeda1_x + '-BRL'
    
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/' + moeda_api)
    
    cotacao = requisicao.json()
    
    #print(cotacao)
     
    moeda=cotacao[moeda1_x]['name']
    data_cotacao=cotacao[moeda1_x]['create_date']
    valor_atual=cotacao[moeda1_x]['bid']
 
    l_moeda['text'] = moeda
    l_data['text'] = data_cotacao
    l_valor['text'] = valor_atual

# Criação tela
janela = Tk()
janela.title('Cotação de moedas')
janela.geometry('320x350')
janela.configure(bg=fundo)

################# Frames ####################

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frameP = Frame(janela, width=320, height=70,bg=cor1, pady=0, padx=0, relief="flat",)
frameP.grid(row=1, column=0)

frameQ = Frame(janela, width=320, height=300,bg=fundo, pady=12, padx=0, relief="flat",)
frameQ.grid(row=2, column=0, sticky=NW)

style = ttk.Style(frameP)
style.theme_use("clam")

# Label da moeda
l_moeda1 = Label(frameP, text='Moeda', height=1, font=('Arial 12'), bg='white')
l_moeda1.place(x=0, y=10)

moeda_selecionada = StringVar()
caixa_combo_moeda1 = ttk.Combobox(frameP, textvariable=moeda_selecionada)
caixa_combo_moeda1['values']=lista_moeda
caixa_combo_moeda1.place(x=120, y=10, width=60, height=25)

#CONVERSOR
l_moeda1 = Label(frameP, text='Conversor', height=1, font=('Arial 12'), bg='white')
l_moeda1.place(x=0, y=40)
e_local = Entry(frameP, font=(l_fonte, 12), relief='solid', bg=cor1, fg=cor3)
e_local.place(x=120, y=40, width=100, height=25,)


#caixa_combo_moeda1.bind('<Return>', info)

b_cotacao = Button(frameP, command=info, text='Cotação', height=1, bg=cor1, fg=cor2, font=('Bernard 9 bold'), relief=RAISED, overrelief=RIDGE)
b_cotacao.place(x=250, y=10)

# Mostra cotação
lb_moeda = Label(frameQ, text="Descrição da moeda", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14 '), bg=fundo, fg=co0)
lb_moeda.place(x=10, y=4)

l_moeda = Label(frameQ, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=cor1)
l_moeda.place(x=15, y=34)

lb_data = Label(frameQ, text="Data cotação", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14'), bg=fundo, fg=co0)
lb_data.place(x=10, y=64)

l_data = Label(frameQ, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=cor1)
l_data.place(x=15, y=94)

lb_valor = Label(frameQ, text="Valor da cotação", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14 '), bg=fundo, fg=co0)
lb_valor.place(x=10, y=124)

l_valor = Label(frameQ, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 20'), bg=fundo, fg=cor1)
l_valor.place(x=15, y=150)

imagem = Image.open('Dolar.png')
imagem = imagem.resize((130, 130), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)
l_icon1 = Label(frameQ,image=imagem, compound=LEFT,  bg=fundo, fg="white",font=('Ivy 10 bold'), anchor="nw", relief=FLAT)
l_icon1.place(x=160, y=130)

janela.mainloop()
