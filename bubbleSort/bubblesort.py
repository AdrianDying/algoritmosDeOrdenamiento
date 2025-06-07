# Creamos la clase

class ObjetoMinecraft:
    def __init__(self, nombre, tipo): #instanciamos el constructor
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self): #__str__nos da el texto en cadena
        return f"{self.nombre} ({self.tipo})"

    # Comparación por nombre
    def __gt__(self, otro): #Permite definir cómo se comparan dos objetos de una clase personalizada utilizando el operador >.
        return self.nombre > otro.nombre

#Funciones del Bubble sort
# Bubble Sort por nombre (usa __gt__ en ObjetoMinecraft)


def bubble_sort_por_nombre(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):     #Compracion j, hace la comparacion alfabetica
            if lista[j] > lista[j + 1]:   # Compara objetos usando __gt__
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Bubble Sort por tipo (compara atributo tipo)
def bubble_sort_por_tipo(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].tipo > lista[j + 1].tipo:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # Este es el que realiza el intercambio


# Lista de objetos a ordenar en el cofre!
objetos = [
    ObjetoMinecraft("Diamante", "Mineral"),
    ObjetoMinecraft("Redstone", "Mineral"),
    #ObjetoMinecraft("Redstone", "Circuito"),
    ObjetoMinecraft("Pico", "Herramienta"),
    ObjetoMinecraft("Repetidor", "Circuito"),
    ObjetoMinecraft("Espada", "Herramienta"),
    ObjetoMinecraft("Zanahoria", "Comida"),
    ObjetoMinecraft("EnderPearl", "Objeto"),
    ObjetoMinecraft("Poción", "Consumible"),
    ObjetoMinecraft("AntorchaRedStone", "Circuito"),
    ObjetoMinecraft("Pan", "Comida")
]

#LosPrints

print("Cofre desordenado:") #PreOrden
for obj in objetos:
    print(obj)

bubble_sort_por_nombre(objetos) #PostOrdenPorNombre
print("\nCofre ordenado por nombre!:")
for obj in objetos:
    print(obj)

bubble_sort_por_tipo(objetos) #PostOrdenPorTipo
print("\nCofre ordenado por tipo de objeto:")
for obj in objetos:
    print(obj)
