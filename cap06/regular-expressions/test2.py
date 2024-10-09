import re

texto = 'Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com'

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)

print(emails)

text = 'O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender.'

# Extraindo os advérbios da frase
for m in re.finditer(r'\w+mente\b', text):
  print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

# REGEX com ChatGPT

# Música: Tempo Perdido

# Legião Urbana

music = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

# 1 - Crie um REGEX para contar quantas vezes o caracter "a aparece em todo o texto da música
count_a = len(re.findall(r'a', music, re.IGNORECASE))

print('O caractere "a" aparece', count_a, 'vezes na música.')

# 2 - Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música
count_word_time = len(re.findall(r'\btempo\b', music, re.IGNORECASE))

print(f'A letra "tempo" aparece {count_word_time} vezes na música')

# 3 - Crie um REGEX em Python para extrair as palavras seguidas por exclamação
exclamations_words = re.findall(r'\b\w+!+', music)

print('Palavras seguidas por exclamação: ', exclamations_words)

# 4 - Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto
extraction = re.findall(r'esse (\w+) amargo', music)
print(f'Palavras cujo antecessor é "esse" e sucessor é "amargo": ', extraction)

# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento

# Encontrando caracteres antes do acento
accented_words = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', music)

print('Caracteres antes do acento: ', accented_words)