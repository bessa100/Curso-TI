import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

cotacao = requisicao.json()
#print(cotacao)
#print('### Cotação do dólar ###')
print('Moeda ' + cotacao['USD']["name"])
print('Data' + cotacao['USD']['create_date'])
print('valor atual: R$ ' + cotacao['USD']['bid'])