#Entrada
valor_compra = float(input("Digite o valor da compra: R$ "))

#Verificação de condições e desconto
if valor_compra < 200:
    print("Você ganhou um desconto de 5%!")
    p = (valor_compra * 5) / 100
    p_final = valor_compra - p 
elif valor_compra >= 200 and  valor_compra <300:
    print("Você ganhou um desconto de 10%!!") 
    p = (valor_compra * 10) / 100
    p_final = valor_compra - p 
else:
    print ("Você ganhou um desconto de 15%")
    p = (valor_compra * 15) / 100
    p_final = valor_compra - p

## Exibição do desconto e valor final
print(f"O valor da sua compra será de: R$ {p_final:.2f} ")
