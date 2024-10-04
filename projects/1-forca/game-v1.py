import random
from os import system, name

# Função para limpar a tela a cada execução
def clean_screen():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

def game():
    clean_screen()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    words = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    word = random.choice(words)

    # Adicionando underline para cada letra da palavra
    letters_guessed = ['_' for letter in word]

    # Tentativas restantes
    attempts_remaining = 6

    # Letras incorretas
    incorret_words = []

    while attempts_remaining > 0:
      print(' '.join(letters_guessed))
      print('\nTentativas restantes:', attempts_remaining)
      print('Letras erradas:', ''.join(incorret_words))

      attempt = str(input('\nDigite uma letra: ').lower())

      if attempt in letters_guessed or attempt in incorret_words:
        print('Você já tentou essa letra. Por favor, tente outra.')
        continue

      if attempt in word:
        index = 0

        for letter in word:
          if attempt == letter:
            letters_guessed[index] = letter
          index += 1
      else:
        attempts_remaining -= 1
        incorret_words.append(attempt)
      
      if "_" not in letters_guessed:
         print('\nVocê venceu, a palavra era:', word)
         break
      
    if "_" in letters_guessed:
       print('\nVocê perdeu, a palavra era:', word)

if __name__ == '__main__':
   game()
   print('\nParabéns. Você é estudado!')