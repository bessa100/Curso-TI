numeros = int(input("Digite um número.: ")) #Declarando a tupla
contador_par = 0
contador_impar = 0
for i in range(0,numeros):
        if i % 2 == 0:
            contador_par=contador_par+1
        else:
            contador_impar=contador_impar+1
print("Quantidade de números pares:",contador_par)
print("Quantidade de números impares:",contador_impar)
