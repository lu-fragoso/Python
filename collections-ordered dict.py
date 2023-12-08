"""

OrderedDict

"""

from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns
# Em um dicionário a ordem de inserção dos elementos não é garantida
dict1 = {'a':1, 'b':2}
dict2 = {'b':2, 'a':1}

print(dict1 == dict2) # True -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict -> A ordem de inserção dos elementos é garantida
odict1 = OrderedDict({'a':1, 'b':2})
odict2 = OrderedDict({'b':2, 'a':1})
print(odict1 == odict2) # False -> A ordem dos elementos








