# input() = uma função que solicita que o usuário insira um dado
# retorna os dados inseridos como uma cadeia de caracateres

name = input("Qual é o seu nome?: ")
age = int(input("Qual é a sua idade?: "))
height = float(input("Qual é a sua altura?: "))

age += 1

print(f"Olá, {name}!")
print("FELIZ ANIVERSÁRIO!")
print(f"Você tem {height} de altura")
print(f"Você tem {age} anos de idade")