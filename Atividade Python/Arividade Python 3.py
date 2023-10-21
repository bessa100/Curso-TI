num = int(input('Digite um número: '))
cont = 0
print('-='*20)
print(f'tabuada do {num}')
while cont != 10:
    cont+= 1
    print(f'{num} x {cont} = {num * cont}')
print('-='*20)