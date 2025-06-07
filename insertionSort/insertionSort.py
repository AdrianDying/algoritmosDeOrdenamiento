#Para la función insertionSort

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave: #Mover elementos mayores hacia adelante
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave


objetos_minecraft = ["Diamante", "Redstone", "Pico", "Repetidor", "Espada", "Zanahoria", "EnderPearl", "Poción", "AntorchaRedStone", "Pan"]


print("Objetos en el cofre:")
for obj in objetos_minecraft:
    print(obj)

insertion_sort(objetos_minecraft)

print("\nAhora tu cofre esta ordenado")
for obj in objetos_minecraft:
    print(obj)
