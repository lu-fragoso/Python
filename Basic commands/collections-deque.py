"""
Deque
"Listas"
"""

from collections import deque

# Criando deques

deq = deque('UxOpen')
print(deq)

# Adicionando elementos no deque

deq.append('Solutions')
print(deq)

deq.appendleft('Invent')
print(deq)

# Remover elementos

print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)

