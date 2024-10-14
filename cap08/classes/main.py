# Criando uma classe chamada Livro
class Livro():
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self):
        
        # Atributos são propriedades 
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe.")
        
    # Métodos são funções que executam ações nos objetos da classe
    def imprime(self):
        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))
    
# Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("O Poder do Hábito", 77886611)

# Método do objeto Livro2
Livro2.imprime("O Poder do Hábito", 77886611)

# Criando a classe 
class Algoritmo():
    
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")

# Criando um objeto a partir da classe 
algo1 = Algoritmo(tipo_algo = 'Random Forest')

# Criando um objeto a partir da classe 
algo2 = Algoritmo(tipo_algo = 'Deep Learning')

# Atributo da classe
algo1.tipo
# 'Random Forest'

algo2.tipo
# 'Deep Learning'