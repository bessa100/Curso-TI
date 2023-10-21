num1 = int(input("Número um: "))
num2 = int(input("Número dois: "))
num3 = int(input("Número três: "))

if num1 < num2 and num3:
    print("O número um é o menor: ", num1)
elif num2 < num1 and num3:
    print("O número dois é o menor: ", num2)
elif num3 < num1 and num2:
    print("O número três é o menor: ", num3)