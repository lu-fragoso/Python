"""
módulo de collections 

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a 
quantidade de ocorrências desse elemento.



"""

# Importando

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma lista
list = [1,1,2,6,64,4,6,64,0,0,9,0,4]

# Utilizando o Counter
res = Counter(list)

print(type(res))

print(res)
# Counter({0: 3, 1: 2, 2: 1, 4: 2, 6: 2, 9: 1, 64: 2})
# Counter criou uma chave e colocou como valor a quantidade de ocorrências.


# Exemplo 2

print(Counter('UxOpen  Solution Invent Company'))   


# Exemplo 3


texto = """
Um texto sobre carros...

Acho que todo homem que se preze ja teve uma paixão por algum carro, mesmo não tendo um, sempre há um modelo que nos chama atenção.
Comigo não foi diferente, eu ja tive o prazer de desfrutar o conforto de alguns, uns mais marcantes do que outros, porém todos únicos.
Poucos tem o privilégio de começar por um padrão alto,um carro caro de muita elegância e desejado por todos, no meu caso eu comecei por baixo, contarei sobre os mais marcantes.
O meu primeiro carro, era engraçado, compacto e pouco notável, para mim era especial pois nele eu dei minhas primeiras voltas e realizei as primeiras loucuras, certo tempo eu fiquei, era apegado, pois ele era meu primeiro carro.
Sobre o segundo carro, eu ja era apaixonado, nunca tinha visto tanto brilho na vida, a elegância e a segurança eram impecáveis, o mais potente e o maior laço que eu faria na vida, eu era louco por ele. Com meu segundo carro eu pude viajar, pude planejar coisas, comprei acessórios, moldei ele a minha maneira, nossa que carro fantastico eu pensava.
Certo dia, resolvi sair, peguei minha paixão, e fomos passear, 5 longos anos se passaram e eu com o mesmo carro, ainda havia encanto e admiração,mas eu, sendo homem tolo, com instinto insaciável, passei à admirar outros carros.
"""

palavras = texto.split()

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))



