import numpy as np

#GLOBAL
mi_arreglo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Arreglo original:", mi_arreglo)
#GLOBAL



#TODOFUNCION UNO
def uno()->None:
    mi_lista = np.array([1,2,3,4,5,'hola',True])
    print(f'Elemento: {mi_lista}. TIPO:{type(mi_lista[0])}')


#TODO FUNCION DOS
def dos()->None:
    #Sumo 5 a cada elemento:
    mi_arreglo_suma = mi_arreglo + 5 #!Se pueden usar todas las operaciones (*,/,**,-,+,etc) por elemento
    print(f'Arreglo elementos +5: {mi_arreglo_suma}')

#TODO FUNCION TRES
def tres()->None:
    #Acceder al primer y último elemento:
    primero = mi_arreglo[0]
    ultimo = mi_arreglo[-1]
    print("Primero:", primero, "Último:", ultimo) #?FORMA NUEVA DE FORMATEAR!!!!

#TODO FUNCION CUATRO
def cuatro()->None:
    primeros_cinco = mi_arreglo[:5]
    print("Primeros 5 elementos:", primeros_cinco)
    print("Ultimos 5 elementos:", mi_arreglo[5:])
    print("Tres elementos del medio:", mi_arreglo[3:6])




#CORRIDA PRINCIPAL
def main()->None:
    cuatro()
if __name__ == "__main__":
    main()