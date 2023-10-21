from tkinter import *
from webbrowser import BackgroundBrowser
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno

#Declaração de variáveis
global imagem, erro1, sigla_moeda

co0 = "#444466" # Preta
co1 = "#feffff" # branca
co2 = "#6f9fbd" # azul

erro1 = 0
sigla_moeda = 'USD'

lista_moedas = ['USD', 'EUR', 'ARS', 'JPY', 'BOB', 'CLP', 'COP']

fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb36d"

fundo = fundo_dia

# Funções
def ver_cotacao():
    moeda_escolhida = caixa_combo_moeda1.get()
    moeda_api = moeda_escolhida + '-BRL'
    
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/' + moeda_api)

    cotacao = requisicao.json()
  
    #print(coracao)
      
    moeda=cotacao[moeda_escolhida]['name']
    data_cotacao=cotacao[moeda_escolhida]['create_date']
    valor_atual=cotacao[moeda_escolhida]['bid']
    
    l_moeda['text'] = moeda 
    l_data['text'] = data_cotacao
    l_valor['text'] = valor_atual
    
# Janela principal
janela = Tk()
janela.title('Cotação de moedas')
janela.geometry('320x450')
janela.configure(bg=fundo)

frame1= Frame(janela, bg='white', width=425, height=385)
frame2= Frame(janela, bg='white', width=425, height=385)
frame1.place(x=0, y=0)
frame2.place(x=425, y=0)

################# Frames #####################

ttk.Separator(janela, orien=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_principal = Frame(janela, width=320, height=70, bg=co1, pady=0, padx=0, relief="flat",)
frame_principal.grid(row=1, column=0)

frame_quadros = Frame(janela, width=320, height=400, bg=fundo, pady=12, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

style = ttk.Style(frame_principal)
style.theme_use("clam")

# Label da moeda
l_moeda1 = Label(frame_principal, text='Moeda', font=('Arial 12'), bg='white')
l_moeda1.place(x=0, y=10)

#Combo-box para selecionar a moeda a ser convertida
moeda_selecionada = StringVar()
caixa_combo_moeda1 = ttk.Combobox(frame_principal, textvariable=moeda_selecionada)
caixa_combo_moeda1['values']=lista_moedas
caixa_combo_moeda1.place(x=65, y=10, width=.60, height=25)

b_cotacao = Button(frame_principal, command=ver_cotacao, text='Cotação', height=1, bg=co1, fg=co2, font=('Arial 12 bold'), relief=RAISED)
b_cotacao.place(x=250, y=10)

# FRAME 1 
print = Label(janela, text='Descrição da moeda', fg='dark blue', bg='light blue', font=('','14'))
print.place(x=20,y=80)
cotacao = ("moedas", "USD", "name")
print = Label(janela, text='Dólar Americano Real Brasileiro', fg='white', bg='light blue', font=('','12'))
print.place(x=30, y=120)

print = Label(janela, text='Data cotação', fg='dark blue', bg='light blue', font=('','14'))
print.place(x=20,y=160)
print = Label(janela, text='', fg='white', bg='light blue', font=('','14'))
print.place(x=30,y=200)

print = Label(janela, text='Valor da cotação', fg='dark blue', bg='light blue', font=('','14'))
print.place(x=20,y=240)

print = Label(janela, text='5.3906', fg='white', bg='light blue', font=('','16'))
print.place(x=30,y=280)

janela.mainloop()