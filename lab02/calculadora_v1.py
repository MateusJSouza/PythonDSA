# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que aprendeu nos capítulos até aqui do curso.

print("\n************** Calculadora em Python **************")

def sum(a, b):
  return a + b

def subtract(a, b):
  return a - b

def divide(a, b):
  return a / b

def multiply(a, b):
  return a * b

option = int(input("\nSelecione o número da operação desejada: \n\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n\nDigite sua opção (1/2/3/4): ")) 

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("\nDigite o segundo número: "))

if option == 1:
    print(f"\n{num1} + {num2} = {sum(num1, num2)}")
elif option == 2:
    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
elif option == 3:
    print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
elif option == 4:
    print(f"\n{num1} / {num2} = {divide(num1, num2)}")
else:
    print("\nOpção inválida!")



