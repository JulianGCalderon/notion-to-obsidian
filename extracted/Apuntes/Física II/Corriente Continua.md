# Corriente Continua

Hasta el momento estudiamos los campos electroestáticos, es decir, el campo generado por cargas estáticas, con velocidad nula.

La corriente continua o **CC** ocurre cuando las cargas dentro de los conductores se mueven a velocidad constante, los electrones se mueven siempre en la misma dirección. Ocurre en los circuitos eléctricos

El campo eléctrico dentro del conductor es nulo solo si se encuentra en *equilibrio estático.*

En los casos de corriente continua, el conductor nunca llega al estado de equilibrio, pero si alcanza el estado estacionario. Es decir, la corriente eléctrica es constante.

# Modelo de Drude

El modelo de Drude fue desarrollado para explicar las propiedades de transporte de electrones en conductores.

Por un lado tenemos iones (positivos), pesados y estáticos. Por el otro lado, electrones (negativos) en movimiento que se aceleran y gana energía cinética. Estos electrones se van a chocar con los iones, se dispersan y pierden parte de su energía. Como resultado de estos choques, el electron ira acelerando y frenando. Alcanzamos una velocidad promedio en sentido de la corriente llamada *velocidad de arrastre o deriva*.

$$
\vec v_a = \frac{q\,\tau}{m}\,\vec E = \mu\,\vec E \qquad\approx 10^{-4} m/s
$$

Llamamos $\tau$ (tau) al tiempo promedio entre los choques, Los parámetros de esta fórmula dependen del material y de la temperatura. Podemos agrupar estos parámetros en $\mu$ (mu), la movilidad.

$$
\text{Movilidad}:\mu = \frac{q\,\tau}{m}
$$

# Corriente Eléctrica

Como históricamente, se relaciono la corriente con la cargas positivas, vamos a estudiar el movimiento de las cargas positivas, a diferencia del modelo de Drude.

La corriente eléctrica es el flujo de carga eléctrica que recorre un material. La podemos definir como como la cantidad de cargas que fluye por unidad de tiempo, aunque también la podemos definir en función del numero de portadores de carga por unidad de volumen ($n$) 

$$
I = \frac{dq}{dt} \qquad [i] = C/s = A_{\color{gray}\text{(Ampere)}}
$$

- $vol\ por\ dt := A\cdot v_a\cdot dt$
- $dq := n\cdot vol\cdot q$

- $n := \frac{Nº \text{ portadores de }q}{\text{unidad de vol.}}$

A partir de estas relaciones, podemos llegar a una ecuación que relacione la corriente eléctrica con la velocidad de arrastre

$$
I = q\cdot n\cdot A \cdot \vec v_a
$$

La corriente tiene un escalar, su valor, y un sentido. Indica el sentido del movimiento de las cargas positivas.

La corriente no tiene porque ser uniforme en todo el conductor, por lo que definimos la $\vec J$ como la densidad volumétrica de corriente. 

Esta densidad es volumétrica ya que el conductor es un volumen, pero es por unidad de area (area de un corte transversal del conductor)

$$
\vec j(\vec r) = q\cdot n\cdot \vec v_a \qquad [j] = A/m^2
$$

$$
I = \oiint\limits_A \vec j(\vec r) \ dA
$$

**¿Quien Genera el Campo Eléctrico?:** El campo es uniforme a lo largo del conductor, ya que ninguno de sus parámetros cambia a lo largo del tiempo. Además, la dirección del campo eléctrico sigue el contorno del conductor.

# Ecuación de Continuidad

Se deduce a partir de una de las ecuaciones de Maxwell

$$
\underbrace{\oiint\limits_A \vec J \cdot dA = -\frac{\partial}{\partial t} \cdot \iiint\limits_{V(S)} \rho\ dv}_\text{Forma Integral}
$$

$$
\underbrace{\vec \nabla \cdot \vec J = -\frac{\partial\rho}{\partial t}}_\text{Forma Diferencial}
$$

La ecuación de continuidad indica que si tenemos corriente eléctrica neta saliendo de una region, la carga en este region tiene que estar disminuyendo

Para corrientes estacionarias, se cumple que toda corriente que entra a un volumen cerrado, sale.

$$
\oiint\limits_S \vec J \cdot ds = 0
$$

$$
\vec \nabla \cdot \vec j = 0
$$

# Ley de Ohm

Así como relacionamos la corriente eléctrica con el campo eléctrico, también podemos relacionar la densidad de corriente eléctrica con el campo.

$$
\vec J = q\cdot n\cdot \frac{q\cdot \tau}{m} \cdot \vec E
$$

Si agrupamos estos parámetros en la conductividad eléctrica $\sigma$, llegamos a la ley de Ohm, en su forma diferencial o local. *(ley de ohm microscópica)*

$$
\boxed{\vec J = \sigma \cdot \vec E}
$$

Podemos deducir entonces, cuanto menor sea la conductividad eléctrico, mayor debe ser el campo eléctrico para llegar a la misma densidad de corriente.

Si analizamos el caso de un conductor cilindro uniforme, llegamos a la forma integral de la ley de Ohm

$$

\Delta V = E\cdot l = \frac{I}{\sigma \,A}\ l = I\,\eta\ \frac{l}{A}\\\ \\
\footnotesize \color{gray}E = J/\sigma \implies J = I/A \implies E = \frac{I}{\sigma A}
$$

$$
\small\text{Resistividad Electrica}:\normalsize \eta= \frac 1\sigma
$$

$$
\small{\begin{align*}
\text{Resistencia Electrica de} \\
\text{un Conductor Cilindrico}
\end{align*}}
\normalsize

: R = \eta\ \frac{l}{A}
$$

La unidad de la resistencia es de Ohm $[R] = \Omega$

Llegamos entonces a la ley de Ohm en su forma integral *(ley de ohm macroscópica)*. Se le llama así porque se calcula a partir de valores que podemos medir macroscópicamente.

$$
\boxed{\Delta V = I\ R}
$$

Notamos que a mayor longitud del cilindro o menor área, la cantidad de choques es mayor. Por lo que la resistencia es mayor.

<aside>
💡 Al atravesar una resistencia, el potencial cae si lo hacemos en el sentido de la corriente

</aside>

# Dependencia de Temperatura

**A mayor temperatura:**

- $\tau:$ Disminuye, hay mas choques entre partículas.
- $v_a:$ Disminuye, al haber mas choques la velocidad es menor.
- $I:$ Disminuye, menos velocidad equivale a menos corriente.
- $\sigma:$ Disminuye, al haber menor corriente, hay menos conductividad eléctrica.
- $\eta:$ Aumenta, la resistividad eléctrica está definida como el inverso de la conductividad eléctrica.

Parece ser que a mayor temperatura, es peor el conductor

**Materiales Conocidos:**

- **Conductor Ideal**: Conductividad tiene a infinito
- **Aislante Ideal:** Conductividad tiende a nulo