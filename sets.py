"""
Conjuntos - Sets

- igual a matemática para analise de dados.

- valores não duplicados
- valores não ordenados
- valores não indexados

utilizados para armazenasr dados sem se importar com suas ordens

Sets {} != maps {}

maps -> chave/valor
set -> valor

informações duplicadas não serão demonstradas

"""

# Definindo um set 

#forma 1
s = set({1,2,3,4,5,6,7,2,2,3})
print(s)
print(type(s))

#forma 2
s = {1,2,4,5,6,7,2,2}
print(s)
print(type(s))

if 3 in s:
    print('tem')
else:
    print('não tem')    

# valores não são ordenados

lista = [99,2,34,23,12,1,44,5,66,77,88,99,34,23]
print(f'lista: {lista}')

tupla = (99,2,34,23,12,1,44,5,66,77,88,99,34,23)
print(f'tupla: {tupla}')

dicionario = {}.fromkeys(lista, 'dict')
print(f'dicionario: {dicionario}')  

conjunto = {99,2,34,23,12,1,44,5,66,77,88,99,34,23}
print(f'conjunto: {conjunto}')


# tipos de dados
s = {1,'b',True, 32.11,-2}
print(s)


# uso de set
Estados = ('SP', "MG", "BA", "TO", "MS", "RS", "BA", "TO")
print(len(Estados))
print(len(set(Estados)))

#ignorando elementos duplicados
conj = {1,2,3}
conj.add(4)
conj.add(4)
print(conj)

#formas de remoção de elementos
#forma 1 - elemento em si sem index
conj.remove(4)
print(conj)

#forma 2 - index
conj.discard(2)
print(conj)


#copiando conjuntos
#forma 1 - deep copy
s  = {1,2,3,4}
novo = s.copy()
print(novo)
novo.add(5)
print(novo)
print(s)

#forma 2 - shallow copy

s  = {1,2,3,4}
novo = s
print(novo)
novo.add(7)
print(novo)
print(s)


#exemplo de caso

python = {"lucas", "pedro", "jose", "marcos"}
java = {"lucas", "marcos", "julia", "roberta", 'ana'}

#forma 1
unio = python.union(java)
print(unio)

#forma 2
unio = python | java
print(unio)

#verificando elementos iguais
#forma 1
inter = python.intersection(java)
print(inter)

#forma 2
inter = python & java
print(inter)


#verificando elementos diferentes -> item 1 - item 2
#forma 1
diff = python.difference(java)
print(diff)

#forma 2
diff = java - python
print(diff)  


#soma, max, min, len
s = {1,2,3,4,5,6,7,8,9}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))










