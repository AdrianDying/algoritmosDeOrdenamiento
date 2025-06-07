#Lista de objetos minecraft
objetos_minecraft = ["Diamante", "Redstone", "Pico", "Repetidor", "Espada", "Zanahoria", "EnderPearl", "Poción", "AntorchaRedStone", "Pan"]

# Función Merge Sort
def merge_sort(lista):
    if len(lista) <= 1: #Esta comparación verifica si la lista tiene mas de 1 elemento, si solo tiene uno, pues ya estaria ordenado
        return lista

    mid = len(lista) // 2 #Con mid definimos la media de la lista para dividir en 2 la lista original
    izquierda = merge_sort(lista[:mid])
    derecha = merge_sort(lista[mid:])

    return merge(izquierda, derecha) #rdse vuelve a llamar

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # el algoritmo
    while i < len(izquierda) and j < len(derecha): #Despues de la division, se compara los minimos de la izquierda con el minimo de la derecha
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1


    resultado.extend(izquierda[i:]) #extend() añade los elementos de un iterable al final de la lista
    resultado.extend(derecha[j:]) #appendo() solo añadiria 1 elemento
    return resultado

#Los prints
print("Estos son tus objetos en el cobre:", objetos_minecraft)

lista_ordenada = merge_sort(objetos_minecraft)

print("El cofre a quedado ordenado", lista_ordenada)
