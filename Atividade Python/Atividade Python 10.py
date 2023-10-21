num = int(input('Digite até qual número quer a sequência: '))
t1 = 0
t2 = 1
cont = 3
t3 = 0
print('0 \n1')

while cont<=num:
    t3 = t1+t2
    print(f'{t3} \n')
    t1 = t2
    t2 = t3
    cont += 1