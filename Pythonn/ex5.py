salario_recebido=float(input("\n Informe seu salário: ")) 
total=float(input(" Informe o total de seus gastos: ")) 
if(salario_recebido>=total):    
    print("-- Gastos dentro do Orçamento") 
else:    
    print("-- Orçamento estourado")