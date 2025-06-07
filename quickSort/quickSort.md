🆀🆄🅸🅲🅺 🆂🅾🆁🆃

 Selecciona un pivote, divide la lista en menores y mayores al pivote, y ordena recursivamente.

El pivote es un elemento de la lista que se utiliza para dividir la lista en dos sublistas: una con elementos menores que el pivote y otra con elementos mayores que el pivote. La posición final del pivote en la lista ordenada se utiliza para dividir la lista en sublistas para llamadas recursivas posteriores. 

     [Diamante, Redstone, Pico, Repetidor, Espada]

 Paso 1: Como en el código, seleccionamos como pivote el ultimo elemento en la lista: Espada

Comparamos, menos a la izquierda, Mayores a la derecha

Por la izquierda 

Espada > Diamante

Por la Derecha 

Espada < Redstone
Espada < Pico
Espada < Repetidor

Por lo tanto

    [Diamante][Espada][Redstone, Pico, Repetidor]

Paso 2

Seleccionamos pivote por la izquierda: Diamante

No tiene elementos para comparar

    [Diamante]

Seleccionamos pivote por la derecha: Repetidor

Comparamos menores por la izquierda mayores a la derecha

   [Redstone, Pico, Repetidor]

Repetidor > Redstone
Repetidor > Pico

por lo tanto

    [Pico][Redstone][Repetidor]

Paso 3 y 4 los pivotes no tienen elementos comparar entonces tenemos que

    [Diamante][Espada][Pico][Redstone][Repetidor]

Pas0 5 se realiza el merge

    [Diamante, Espada, Pico, Redstone, Repetidor]
