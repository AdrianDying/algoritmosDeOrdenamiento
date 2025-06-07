
🅸🅽🆂🅴🆁🆃🅸🅾🅽🆂🅾🆁🆃

Toma elementos uno por uno y los inserta en la posición correcta dentro de una lista ordenada parcial.

[Diamante, Redstone, Pico, Repetidor, Espada]

Paso 1:
Tomamos = Redstone
Redstone" > Diamante, no se mueve


    [Diamante, Redstone, Pico, Repetidor, Espada]

Paso 2:
Tomamos = Pico
Pico < Redstone, se recorre

Pico" > "Diamante", no se mueve

    [Diamante, Pico, Redstone, Repetidor, Espada]

Paso 3:
Tomamos = Repetidor
Repetidor < Redstone, se recorre
Repetidor > Pico, no se mueve

    [Diamante, Pico, Repetidor, Redstone, Espada]

Paso 4:
Tomamos = Espada
Espada < Redstone, recorremos
Espada < Repetidor, recorremos
Espada < Pico, recorremos
Espada >  Diamante, no se mueve

**[Diamante, Espada, Pico, Repetidor, Redstone]**
