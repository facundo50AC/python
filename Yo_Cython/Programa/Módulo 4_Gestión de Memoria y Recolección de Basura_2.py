import gc

def crear_listas():
    listas = []
    for i in range(10):
        listas.append([j for j in range(1000)])
    return listas

# Crear listas
mis_listas = crear_listas()

# Eliminar algunas referencias
del mis_listas[0:5]

# Forzar la recolección de basura y ver los objetos recolectados
gc.collect()

# Verificar la memoria liberada (esto puede variar según el sistema y el entorno de ejecución)
import sys
for obj in gc.get_objects():
    if isinstance(obj, list):
        print(f"List of length {len(obj)} still exists in memory")