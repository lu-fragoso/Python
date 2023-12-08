
"""
Funcões são trechos que realizam determiadas tarefas 
Podem ou não retornar um valor.

São muito uteis para executar procedimentos similares por repetidas vezes.

OBS: Se você escrever uma função que realiza varias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

"""
# Exemplo de função sem retorno

cores = ['r','g','b']

def cores_disponiveis():
    print(cores)

cores_disponiveis()

# Exemplo de função com retorno

def soma(a,b):
    return a+b

print(soma(2,3))






