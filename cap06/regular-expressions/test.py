# Expressões regulares são padrões usados para combinar ou encontrar ocorrências
# de sequências de caracteres em uma string. Em Python, expressões regulares são 
# geralmente usadas para manipular strings e realizar tarefas como validação da
# entrada de dados, extração de informações de strings e substituição de texto.

import re

text = 'Meu e-mail é exemplo@gmail.com e você pode me encontrar em outro_email@yahoo.com'

# Expressão regular para contar quantas vezes o caracter arroba aparece no texto
resultado = len(re.findall('@', texto))

print('O caractere "@" apareceu', resultado, 'vezes no texto.')

# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r'você (\w+)', texto)

print('A palavra após "você" é:', resultado[0])

# 1. Verificar se uma string contém um número
def contains_number(string):
    # Expressão regular para verificar se há um dígito na string
    pattern = r'\d'
    return re.search(pattern, string) is not None

# Exemplo de uso
print(contains_number("Olá, mundo!"))  # False
print(contains_number("Olá, mundo 2023!"))  # True

# 2. Extrair todos os endereços de e-mail de um texto
def extract_emails(text):
    # Expressão regular para encontrar endereços de e-mail
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

# Exemplo de uso
text = "Contate-nos em info@exemplo.com ou suporte@teste.com"
print(extract_emails(text))  # ['info@exemplo.com', 'suporte@teste.com']

# 3. Substituir espaços em branco por um único espaço
def normalize_spaces(text):
    # Expressão regular para substituir múltiplos espaços em branco por um único espaço
    pattern = r'\s+'
    return re.sub(pattern, ' ', text)

# Exemplo de uso
text_with_spaces = "Isto    é   um   texto   com   muitos   espaços."
print(normalize_spaces(text_with_spaces))  # 'Isto é um texto com muitos espaços.'

# 4. Validar um número de telefone (formato: (XX) XXXX-XXXX)
def validate_phone_number(phone):
    # Expressão regular para validar o formato de número de telefone
    pattern = r'^\(\d{2}\) \d{4}-\d{4}$'
    return re.match(pattern, phone) is not None

# Exemplo de uso
print(validate_phone_number("(12) 3456-7890"))  # True
print(validate_phone_number("1234567890"))  # False

# 5. Encontrar todas as palavras que começam com uma letra específica
def find_words_starting_with(text, letter):
    # Expressão regular para encontrar palavras que começam com a letra especificada
    pattern = rf'\b{letter}\w*'
    return re.findall(pattern, text, re.IGNORECASE)

# Exemplo de uso
text = "A abelha e a aranha são animais interessantes."
print(find_words_starting_with(text, 'a'))  # ['A', 'abelha', 'a', 'aranha', 'animais']

# Nota: O r antes da string que representa a expressão regular em Python é usado para
# indicar que a string é uma string literal raw. Isso significa que as barras
# invertidas () não são interpretadas como caracteres de escape, mas são incluídas
# na expressão regular como parte do padrão.