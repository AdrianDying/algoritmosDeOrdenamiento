🅷🅴🅰🅿🆂🅾🆁🆃

Convierte la lista en un montículo, extrae el mayor repetidamente y reconstruye el montículo

 El montículo es una estructura de datos tipo árbol que cumple la propiedad del montículo, donde cada nodo es mayor o igual que sus hijos (en un montículo máximo) o menor o igual (en un montículo mínimo). Esta estructura se utiliza para organizar los elementos de la lista de manera que el elemento más grande (o más pequeño) esté en la raíz, lo que facilita la extracción de elementos de forma ordenada

Previa - Asignamos índices a los elementos de la lista

     [Diamante(0), Redstone(1), Pico(2), Repetidor(3), Espada(4)]

Paso 1 Construimos el Max-heap

						Diamante(0)
						/          \
					Redstone(1)      Pico(2)
					/         \
			       Repetidor(3)      Espada(4)

Reorganizamos los hijos ya que de los 3 por la izquierda "Repetidor es el mayor


                                                 Diamante
						/         \
					  Repetidor      Pico
					/         \
			           Redstone      Espada

Reorganizamos otra vez el árbol ya que "Repetidor" es mayor a "Diamante"


                                                 Repetidor - Ahora tenemos el Max Leap
						/         \
					  Diamante      Pico
					/         \
			           Redstone      Espada

Como "Repetidor esta en el máximo lo sacamos y el el elemento final de nuestra lista

     [Repetidor]

Reorganizamos el árbol

					Pico
                                       /    \
				   Diamante Espada
				   /
                                Redstone

Ahora comparamos "Redstone" tiene mayor valor a "Diamante" - Reorganizamos

					Pico
                                       /    \
				 Redstone  Espada
				   /
                                Diamante
Comparamos- Redstone tiene mayor valor a Pico - Reorganizamos

				      Redstone Ahora tenemos el segundo elemento de la lista, lo sacamos del árbol
                                       /    \
				   Pico     Espada
				   /
                                Diamante

    [Redstone, Repetidor]

Reorganizamos

                                      Espada
                                     /     \
                                   Pico    Diamante

Comparamos "Pico" ahora es el de mayor valor

					Pico Sacamos del árbol y tenemos nuestro 3er elemento
					/   \
			       	Espada     Diamante

    [Pico, Redstone, Repetidor]

Reorganizamos

					Diamante
                                          /
				     Espada

Comparamos "Espada" tiene mayor peso que diamante. reorganizamos

					Espada ahora tenemos nuestro 4° y 5° elemento
					/
				    Diamante

[Diamante, Espada, Pico, Redstone, Repetidor]


 
