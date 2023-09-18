"""
Maps = Dicitonary {}
"""
receita = {"jan": 100,"fev":250, "mar":300}

# Interações sobre Maps

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Acessando keys do Map/Dictionary
print (receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando values do Map/Dictionary
print (receita.values())

for valor in receita.values():
    print(valor)

# Desempacotando um Map/Dictionary
print(receita.items())

for chave, valor in receita.items():
    print(f'Chave:{chave} e Valor:{valor}')

# Operações com os valores de um Map/Dictionary 
# Tendo que ser necessariamente do mesmo tipo de dado

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
