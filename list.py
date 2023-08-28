# listas, arrays ou matrizes -> Todos voltados para agrupar dados

lista1 = [13,3,15,7,19,11,13]
lista2 = ['a','b','c','d','e','f']
lista3 = []
lista4 = list(range(11))
lista5 = list('OTGO')

num = 1 

if num in lista4:
    print('Achou')
else:
    print("Não achou")


lista1.sort() #ordenação

print(lista1)
print(lista1.count(13))
print(lista5.count('O'))

# add elementos -> append (para somente a adição de 1 elemento)

lista1.append(27)
print(lista1)

# add no mínimo 2 itens ao final da lista -> extend
lista1.extend([27,28,29])
print(lista1)

# add um item ao local designado -> insert(pos, iten)
lista1.insert(0,1)
print(lista1)

# imprime a lista inversa
lista1.reverse()
print(lista1)

# Copy -> copiar 
lista6 = lista5.copy()
print(lista6)

# len -> verifica o tamanho
print(len(lista2))

# pop -> conceito de pilha(remove o ultimo elemento da lista), ou utilizando o indice para remover
lista1.pop()
lista1.pop(0)
print(lista1)
 
# clear -> limpa a lista
lista6.clear()
print(lista6)





