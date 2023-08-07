# Circuitos Sincronicos

## Flip-Flop D Sincrónico Activado por Nivel

!![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/attachments/Circuitos Sincronicos 3.png]]

El circuito únicamente cambia cuando el pulso del reloj esta habilitado. Si no, el circuito mantiene su valor anterior.

## Flip-Flop JK Sincrónico Activado por Nivel

!![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/attachments/Circuitos Sincronicos 1.png]]

Es un $JK$, pero si $J{=}K{=}1$, únicamente oscila cuando el reloj esta en pulso. Además, no sabemos en que estado va a terminar luego del pulso

## Flip-Flop JK Sincrónico del tipo Maestro-Esclavo

!![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/attachments/Circuitos Sincronicos 2.png]]

Este circuito es la solución mas común a la problemática mencionada anteriormente, si $J{=}K{=}1$, entonces $Q$ oscila a una frecuencia determinada, y cambia de estado en el flanco (descendente) del pulso.