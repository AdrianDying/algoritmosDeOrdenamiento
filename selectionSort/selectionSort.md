🆂🅴🅻🅴🅲🆃🅸🅾🅽🆂🅾🆁🆃

Busca el valor mínimo en una lista y lo intercambia con el primero. Repite con los elementos restantes.

Paso 1:
Buscamos el primero entre los elementos de la lista:

    [Diamante, Redstone, Pico, Repetidor, Espada]

Mínimo: Diamante

Como:
Redstone > Diamante, no cambia
Como:
Pico > Diamante, no cambia
como:
Repetidor > Diamante, no cambia

Espada > Diamante, no cambia

Por lo tanto no hay intercambio y diamante es el mínimo!

    [Diamante, Redstone, Pico, Repetidor, Espada]

Paso 2

Buscamos el mínimo entre:
    [Redstone, Pico, Repetidor, Espada]

Mínimo: Redstone

Como:
Pico < Redstone, nuevo mínimo
Como:
Repetidor > Pico, no cambia
Como
Espada < Pico, se recorre

Intercambiamos Redstone por Espada

    [Diamante, Espada, Pico, Repetidor, Redstone]

Paso 3
Buscamos el mínimo entre:
[Pico, Repetidor, Redstone]

Mínimo: Pico
Como:
Repetidor > Pico, no cambia
Como:
Redstone > Pico, no cambia

    [Diamante, Espada, Pico, Repetidor, Redstone]

Paso 4:
Buscamos el mínimo entre:
[Repetidor, Redstone]

Mínimo: Repetidor
Como:
Redstone > Repetidor, no cambia
Por lo tanto
**[Diamante, Espada, Pico, Repetidor, Redstone]**

