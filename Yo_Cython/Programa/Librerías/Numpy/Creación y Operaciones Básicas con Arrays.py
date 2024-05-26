import numpy as np

lista = np.array([1,2,3,4,5])
print(f'lista con numpy: {lista}')

# Realizar operaciones básicas
print("Suma:", np.sum(lista))
print("Producto:", np.prod(lista))
print("Media:", np.mean(lista))
print("Desviación estándar:", np.std(lista))

# Operaciones vectorizadas
print("lista + 5:", lista + 5)
print("lista * 2:", lista * 2)