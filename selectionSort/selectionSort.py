# Para la función selectionSort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i  # Se asume que el minimo esta en la posición inicial
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j  # Comparativa por valores menores

        lista[i], lista[min_index] = lista[min_index], lista[i] #Este hace el intercambio

# Lista de objetos a ordenar
objetos_minecraft = ["Diamante", "Redstone", "Pico", "Repetidor", "Espada", "Zanahoria", "EnderPearl", "Poción", "AntorchaRedStone", "Pan"]

#Prints

print("Estos son los objetos en tu cofre:") #PreOrder
for obj in objetos_minecraft:
    print(obj)


selection_sort(objetos_minecraft)


print("\nObjetos ordenados correctamente:") #Print post order
for obj in objetos_minecraft:
    print(obj)
