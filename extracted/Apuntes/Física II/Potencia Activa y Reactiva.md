# Potencia Activa y Reactiva

Partimos de la ecuaciones de corriente eléctrica, con fase inicial nulo para simplificar las cuentas.

$$
v_q(t) = v_0 \cdot \cos(wt)
$$

$$
i(t) = i_0 \cdot (wt + \phi_{iv})
$$

Planteamos entonces, la ecuación de la potencia instantánea.

$$
p(t) = v_0\ i_0 \cdot \cos(wt) \cdot \cos(wt +\phi_{iv})
$$

Si calculamos el valor medio (integrando y dividiendo sobre el intervalo), llegamos a la expresión de la potencia media.

$$
\lang p(t) \rang = \frac{v_0\ i_0}{2} \cdot \cos (\phi_{iv} )
$$

Remplazando las amplitudes por sus valores eficaces, entonces:

$$
\lang p(t) \rang =v_{ef}\ i_{ef}  \cdot \cos(\phi_z) =i_{ef}^2 \cdot R
$$

# Potencia Activa y Reactiva

Tambien podemos reescribir la potencia en función de la potencia activa y la reactiva, siendo:

$$
p(t) = \underbrace{v_{ef}\ i_{ef}\cdot\cos(\phi_{iv})}_\text{$P:$ Potencia Activa} \cdot \Big[cos (2wt + 1)\Big] \ \underbrace{- v_{ef} \cdot i_{ef}\cdot \sin(\phi_{iv})}_\text{$Q:$ Potencia Reactiva}\cdot \Big[\sin(2wt)\Big]
$$

Encontramos que la potencia activa representa la potencia media del circuito, asociada con la potencia disipada por la resistencia. Además, relacionamos la potencia reactiva con la reactancia inductiva del circuito, asociada a la potencia almacenada en los inductores o capacitores.

$$
P = v_{ef}\ i_{ef} \cdot \cos(\phi_z)=i_{ef}^2 \cdot R
$$

$$
Q = v_{ef}\ i_{ef} \cdot  \sin(\phi_z) = i_{ef}^2 \cdot (X_L - X_C)
$$

La potencia reactiva no representa el trabajo realizado, es energía que se conserva. Sera la potencia acumulada como energía tanto en el inductor como en el capacitor. Tendrá unidades de $[Q] = VAR$. (Voltio, Ampere, Reactivo)

<aside>
💡 Si $X_L > X_C$, el circuito tendrá un comportamiento inductivo, en el caso contrario, tendrá comportamiento capacitivo.

</aside>

## Triangulo de Potencias

Podemos relacionar entonces las potencias en un triangulo.

!![[Apuntes/Física II/attachments/Potencia Activa y Reactiva 2.svg]]

Llamaremos $S$ a la hipotenusa del triángulo

$$
S = v_{ef} \ i_{ef} \qquad [S] = VA
$$

Si el circuito es resistivo puro $(\phi_z = 0) \iff Q = 0$, por lo que $S = P$

Si el circuito es reactivo puro, $(\phi_z = \pm\pi/2) \iff P = 0$, por lo que $S = Q$

### Potencia Aparente

Llamamos $S$ entonces, a la potencia aparente. La potencia que siente la fuente que tendrá que entregarle al circuito.

### Factor de Potencia

Llamamos $cos(\phi_z)$ al factor de potencia. Un valor que representa la relación entre la potencia disipada (consumida) y la potencia almacenada.

## Triángulos Equivalentes

Si a los lados del triangulo anterior, lo divido por la corriente, encuentro un nuevo triangulo equivalente, con las tensiones del circuito

Si lo vuelvo a dividir por la corriente, llegamos a un triangulo de las reactancias

!![[Apuntes/Física II/attachments/Potencia Activa y Reactiva 1.svg]]