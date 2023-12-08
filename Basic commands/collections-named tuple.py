"""

Named tuple  -> São tuplas onde especeficamos um nme para a mesma e também parâmetros


"""

# Importando
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Utilizando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados
# Forma 1
print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome

# Forma 2
print(ray.idade) # idade
print(ray.raca) # raca
print(ray.nome) # nome

