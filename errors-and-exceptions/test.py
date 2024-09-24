# Erro (leia a mensagem de erro)
print('Hello)

# 2. Tentativa de operação inválida
8 + 's'

# 3. Definição de uma função
def numDiv(num1, num2):
  result = num1 / num2
  print(result)

# 4. Chamada da função sem erro
numDiv(4, 2)

# 5. Chamada da função que gera erro
numDiv(4, 0)

# 6. Uso de try/except para tratar erro
try:
  8 + 's'
except TypeError:
  print('Operação não permitida!')

# 7. Utilizando try/except/else
try:
  f = open('arquivos/testandoerros', 'r')
except IOError:
  print('Erro: arquivo não encontrado ou não pode ser lido.')
else: 
  print('Conteúdo gravado com sucesso!')
  f.close()

# 8. Uso de try/except/else para manipulação de arquivo
try:
  f = open('arquivos/testandoerrors.txt', 'w')
  f.write('Gravando arquivo')
except IOError:
  print('Erro: arquivo não encontrado ou não pode ser salvo.')
else:
  print('Conteúdo gravado com sucesso!')
  f.close()

# 9. Finally
try: 
  f = open('arquivos/testandoerros.txt', 'w')
  f.write('Gravando no arquivo')
except IOError:
  print('Erro: arquivo não encontrado ou não pode ser salvo.')
else:
  print('Conteúdo gravado com sucesso!') 
  f.close()
finally: 
  print('Comandos no bloco finally são sempre executados!')
