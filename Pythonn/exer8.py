texto = input("Entre com uma string: ")
digitos=0
letras=0
for x in texto:
    if x.isdigit():
        digitos=digitos+1
    elif x.isalpha():
        letras=letras+1
    else:
        pass
print("Total de letras: ", letras)
print("Total de Digitos:", digitos)