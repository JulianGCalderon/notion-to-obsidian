# Campo Magnético

Existe en una zona del espacio un campo magnético $\vec B$. Los imanes que generan estos campos tienen dos polos. Un polo norte (positivo) y un polo sur (negativo). Los polos iguales se repelen, mientras que los polos distintos se atraen.

La unidad del campo magnético es de $[\vec V] = T \text{(tesla)} = N/(A\cdot m)$

La tierra tiene asociada un imán, en el polo norte geográfico se encuentra el polo sur magnético e igualmente para el polo sur geográfico.

La utilización mas antigua de los campos magnéticos es la brújula, un imán en equilibrio que se alineara con el campo magnético de la tierra. Por eso el polo norte magnético de la brújula apuntara al polo norte geográfico de la tierra (polo sur magnético)

# Momento Dipolar Magnético

Similar a como se reordenaban los dipolos en un dieléctrico, ocurre algo parecido en los imanes. El momento dipolar magnético $\vec m$ se alinea con el campo magnético.

Sin embargo, a diferencia de un dieléctrico, no podemos monopolizar los polos. Todo imán tiene ambos polos, incluso si los dividimos. Debido a esto, el flujo a través de una superficie cerrada es nulo.

$$
\underbrace{\phi_B = \oiint\limits_S \vec B\ d\vec s = 0}_\text{Campo Solenoidal}
$$

Las líneas de campo son cerradas, todas las que salen del polo norte ingresan al polo sur.

# Fuerza Magnética

La fuerza magnética resulta proporcional a la velocidad de la partícula, la carga, y el campo magnético. Además, es perpendicular tanto al vector velocidad como al vector campo magnético.

$$
\vec F_M = q\cdot \vec v \times \vec B
$$

$$
\vec F_\text{Lorentz} = q\vec E +  q\cdot \vec v \times \vec B
$$

Ya que la fuerza es siempre perpendicular a la trayectoria, entonces el trabajo de la fuerza magnética es nulo. $\vec F_M$ no es conservativa. Ya que no es conservativa, el modulo de la velocidad permanece constante. $W_{Fnc} = \Delta U_{\text{cinetica}}$

## Trayectoria en $\vec B$ uniforme

### Caso 1: $\vec v \perp \vec B$

El movimiento es un **MCU**, movimiento circular uniforme. La fuerza magnética actúa como la fuerza centrípeta.

$$
F_M = qv\cdot B = m \cdot a_c = m\cdot \frac{v^2}{R}
$$

$$
R = \frac{m\cdot v}{q\cdot B}
$$

$$
w = \frac{v}{R} = \frac{q\cdot \vec B}{m}
$$

$$
T = \frac{2\pi\cdot m}{q\cdot B}
$$

### Caso 2: $\vec v \not\perp \vec B$

El movimiento es compuesto, se mueve tanto en **MCU** como en **MRU,** movimiento rectilíneo uniforme. De esta forma, la trayectoria es una hélice (movimiento helicoidal).

Comparte las mismas formulas que el caso anterior, pero se usa la velocidad perpendicular $v_\perp$ al campo para el **MCU**.

Por otro lado, la velocidad paralela $v_\parallel$ al campo afecta el **MRU**. Siendo $h$ el desplazamiento en esta dirección por cada periodo

$$
h = v_\parallel\cdot T = \frac{v_\parallel\cdot 2\pi \cdot m}{q\cdot B}
$$

<aside>
💡 Si la carga es negativa, la trayectoria es la misma pero la fuerza tiene sentido opuesto

</aside>

# Aplicaciones

## Selector de Velocidades

Consiste en una fuente con un campo magnético $\vec B$ y un campo eléctrico $\vec E$ que permite entrar y salir únicamente cargas que realicen una trayectoria rectilínea. Es decir, que la fuerza de Lorentz sea nula.

$$
\|\vec v\| = \frac{\|\vec E\|}{\|\vec B\|}
$$

## Espectrómetro de Masas

Utiliza un selector de velocidades para aislar cargas con la misma velocidad. Ya que las cargas tienen la misma carga y velocidad pero distinta masa, estas se van a girar debido al campo magnético y el radio de giro va a depender de la masa. De esta forma podemos recolectar cargas con diferente de masa dependiendo de la posición.