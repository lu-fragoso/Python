"""

módulo de collections 

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, 
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido. 
Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
"""

#dict = {'curso':'Python'}
#print(dict)
#print(type(dict))


# Importando

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)
print(type(dicionario))

# Adicionando valores
dicionario['curso'] = 'Python'

print(dicionario)

# Acessando um valor desconhecido, ele atribui o valor default
print(dicionario['outro']) # KeyError no dicionário comum

print(dicionario)
