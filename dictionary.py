"""
Dicionário -> pode ser conhecido por mapas

coleção chave:valor (qualquer tipo de dado)

dicionario{} - dict()

tuple() -> um bom exemplo de chave
"""
# forma de criação 1
paises = {'br':"brasil",'eua':"estados unidos",'py':'paraguai'}
print(paises)
print(type(paises)) # mostra o tipo do dicionario

"""
# forma de criação 2
paises = dict(br = 'brasil',eua = 'estados unidos', py = 'paraguai')
print(paises)
print(type(paises)) # mostra o tipo do dicionario
"""

"""
# forma de criação 3 - não usual

usuario = {}.fromkeys(['nome','email','telefone','profile'], 'desconhecido')
print(usuario)
print(type(usuario))

"""

# Acessando elementos 
print(paises['br'])
print(paises['eua'])

print(paises.get('br'))
print(paises.get('usa','Não existe país com esse nome!')) # pode ser utilizado como condicional

# Verificando elementos -> só acessa chaves
print('br' in paises)
print('usa' in paises)
print('brasil' in paises)

# Adicionando elementos no dicionário 
paises['ru'] = 'russia'
print(paises)
paises.update({'pt': 'portugal'})
print(paises)

# Atualizando dados no dicionário

paises['ru'] = 'Russia'
print(paises)
paises.update({'pt':'PORTUGAL'})
print(paises)

# Deletando dados do dicionario
paises.pop('pt')
print(paises)
del paises["ru"]
print(paises)


# Utilização de diferentes métodos para realizar um processo
"""
carrinho de compras = []

produto 1 
    nome 
    quantidade 
    preço
produto 2 
    nome 
    quantidade 
    preço    
"""
# list
carrinho = []
produto1 = ['bola',1,10.00]
produto2 = ['luva',1,20.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# tuple
carrinho = []
produto1 = ('bola',1,10.00)
produto2 = ('luva',1,20.00)

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# dictionary
carrinho = []
produto1 = {'nome':'bola','qtd':1,'valor':10.00}
produto2 = {'nome':'luva','qtd':1,'valor':20.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Métodos com Dicionário
d=dict(a=1,b=2,c=3)

# Copiar 

di = d.copy()
print(di)

# Limpar dados

d.clear()
print(d)



