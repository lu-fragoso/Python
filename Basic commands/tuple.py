"""
Tuples != List

Tuple() - List[]

Tuple() -> Não é possível realizar alterações, quando tenta alterar acaba gerando uma nova tuple() (Imutável) (Pode seobrescrever os valores)

Tuple() -> É definida pelo uma de , e não ()

Tuple() -> Mais rápida que lista

Tuple() -> Segura pois é imutavel

"""
tupla1 = (1,2,3)
print(tupla1)
print(type(tupla1))

tupla2 = 4,5,6,7,8,9
print(tupla2)
print(type(tupla2))

tupla3 = (1)         # Isso é um Inteiro!
print(type(tupla3))

tupla4 = (1,)        # Isso é uma Tupla de 1 elemento
print(type(tupla4))

tupla5 = 'a','b','c','a','b','c','a','b','c','c','c','c'
print(type(tupla5))

# Método Range funciona igual a List
tupla = tuple(range(10))
print(tupla)

# Método de descompactamento funciona igual a List
tupla = "o","t","g"
a,b,c = tupla
print(a,b,c )

# Utilização de Métodos iguais a List contanto que sejam só numerais(operações)
tupla = tuple(range(10))
print(max(tupla))
print(min(tupla))
print(sum(tupla))
print(len(tupla))

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

# Interagindo com a tupla 
for i in tupla1:
    print(i)
for index, value in enumerate(tupla1):
    print(index, value)

# Contando elementos em uma tupla 

print(tupla5.count('c'))

tupla6 = 'Lucas Garcia Fragoso'
print(tupla6.count('a'))

# Utilização de Tuplas
meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

print(meses_do_ano[0])

# Interar com os meses
i=0
while i < len(meses_do_ano):
    print(meses_do_ano[i])
    i+=1

# Verificando qual o Index do valor
print(meses_do_ano.index('Novembro'))


# Separando a Tupla por Slice
print(meses_do_ano[4:11:2])