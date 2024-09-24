# Função Enumerate

# A função enumerate retorna um objeto enumerado, que contém pares de índice e valor

# Criando uma lista
seq = ['a', 'b', 'c']

enumerate(seq)

list(enumerate(seq))

# Exemplo 1: Imprimindo valores de uma lista com a função enumerate() e seus respectivos índices
for indice, valor in enumerate(seq):
    print(indice, valor)

# Exemplo 2: Usando enumerate com uma condição dentro do loop
for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print(valor)

# Exemplo 3: Usando enumerate com uma lista de strings
lista = ['Marketing', 'Vendas', 'TI', 'Comercial']
for i, item in enumerate(lista):
    print(i, item)

# Exemplo 4: Usando enumerate com uma string
for i, item in enumerate('Data Science Academy'):
    print(i, item)

# Exemplo 5: Usando enumerate com um range de números
for i, item in enumerate(range(10)):
    print(i, item)