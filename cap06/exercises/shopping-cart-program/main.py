# Exercício 2 - Programa do carrinho de compras

item = input("Qual item você gostaria de comprar?: ")
price = float(input("Qual é o preço?: "))
quantity = int(input("Quantos você gostaria de comprar?: "))

total = price * quantity

print(f"Você comprou {quantity} x {item}/s")
print(f"O total é R${total}")