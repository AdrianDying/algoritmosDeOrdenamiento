"""Qué es el pivote? el pivote es un elemento de la lista que se utiliza para dividir la lista en dos sublistas:
una con elementos menores que el pivote y otra con elementos mayores que el pivote.
La posición final del pivote en la lista ordenada se utiliza para dividir la lista en sublistas para llamadas recursivas posteriores."""

#Funcion para el quick sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # Esta es la lista ordenada

    pivote = lista[-1] #Por practicidad elegimos el ultimo elemento del pivote!
    menores = []
    mayores = []

    for elemento in lista[:-1]: #una vez termine de comparar el pivote, este sale de la lista y continua con el siguiente tomando otra vez la recursión para el ultimo elemento
        if elemento <= pivote:
            menores.append(elemento)
        else:
            mayores.append(elemento)

    #El merge
    return quick_sort(menores) + [pivote] + quick_sort(mayores) # el merge se usa comparando con un quick sort por la izquierda los menores y por la derecha los mayores en comparación al pivote

# Lista de objetos Minecraft
objetos_minecraft = ["Diamante", "Redstone", "Pico", "Repetidor", "Espada", "Zanahoria", "EnderPearl", "Poción", "AntorchaRedStone", "Pan"
]

print("Estos objetos tienes el cofre:")
print(objetos_minecraft)

ordenada = quick_sort(objetos_minecraft)

print("\nAsí quedo tu cofre despues de pivotear:")
print(ordenada)
