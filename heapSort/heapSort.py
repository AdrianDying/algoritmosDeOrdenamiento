"""heapify() pertenece modulo heapq que permite transformar una lista desordenada en un heap válido.
Un heap es una estructura de árbol binario que satisface la propiedad de heap,
donde el elemento más pequeño (en un montón mínimo) o el más grande (en un montón máximo) está en la raíz"""

""""
1. Reorganiza la lista:
heapify() reorganiza los elementos de la lista original en el lugar, es decir, no crea una copia.
2. Convierta en un heap:
Reorganiza los elementos de la lista para que cumpla con la propiedad del heap. En el caso de un montón mínimo, el elemento más pequeño estará en la raíz.
3. Eficiencia:
La operación se realiza en tiempo lineal, lo que la hace muy eficiente para construir un montón a partir de una lista. """

"""El módulo heapq en Python implementa la estructura de datos de cola de montón o cola de prioridad,
que permite acceder fácilmente al elemento más pequeño (o más grande) de una colección """

import heapq

def heapify(lista, n, i): #se crea el nodo raiz, donde las ramas hijas por la izquierda, tienen que ser menor al indice del max heap por ende, las de la derecha tienen que ser mayores
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda

    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha

    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)

def heap_sort(lista):
    n = len(lista)

    # Para el nodo
    for i in range(n // 2 - 1, -1, -1): # La raíz del max heap contiene siempre el valor más grande.
        heapify(lista, n, i)

    # Despues de la contrucción del max heap, el arreglo acomoda los elementos ordenados segun su comparación
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

# Lista de Objetos dentro del cofre
objetos_minecraft = ["Diamante", "Redstone", "Pico", "Repetidor", "Espada", "Zanahoria", "EnderPearl", "Poción", "AntorchaRedStone", "Pan"]


print("Estos son tus objetos que estan dentro del cofre:")
print(objetos_minecraft)

heap_sort(objetos_minecraft)

print("\nCofre ordenado por el heap sort:")
print(objetos_minecraft)
