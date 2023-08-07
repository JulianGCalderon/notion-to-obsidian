# Materiales Magnéticos

Una particula cargada orbita alrededor de su núcleo. Esto se puede pensar como corriente a través de una espira circular, por lo que tiene un momento angular. Este momento angular se alineará con el campo magnético en ese punto del espacio, por acción de un torque.

Si el campo magnético es débil, entonces la magnetización será parcial. Si el campo magnético es intenso, la magnetización será completa.

Vamos a introducir un nuevo campo vectorial, el campo **magnetización**, denominado $\vec M$. Nos va a indicar la cantidad de momentos angulares por unidad de volumen tenemos

$$
\oint\limits_{\lambda} \vec M \cdot d\vec l = i_m \qquad \vec M = \frac{\delta \vec m}{\delta \text{vol}}
$$

$$
\underbrace{\vec \nabla \times \vec M = \vec J_{m}}_\text{Forma Diferencial}
$$

Estas corrientes de magnetización van a estar asociadas a las corrientes de los electrones que orbitan al alrededor del núcleo de los átomos.

Las corrientes concatenadas de la ley de ampere deben tener en cuenta ambas corrientes, tanto la corrientes de magnetización $i_m$ como las corrientes reales $i_R$.

Llamaremos $\vec H$ al campo magnético relacionado con las corrientes reales, y $\vec B$ al campo de inducción magnética, relacionado con ambas corrientes.

$$
\underbrace{\oint\limits_{\lambda} \vec H \cdot d\vec l = i_R}_\text{Ley de Ampere Generalizada}
$$

$$
\underbrace{\vec \nabla \times \vec H = \vec J_{R}}_\text{Forma Diferencial}
$$

$$
\oint\limits_{\lambda} \vec B \cdot d\vec l = \mu_0\cdot(i_m + i_R)
$$

A partir de estas definiciones, podemos llegar a la **relación constitutiva:**

$$
\vec B = \mu_0\cdot(\vec M + \vec H)
$$

<aside>
💡 El campo de inducción magnética tiene unidades de tesla $T$, mientras que el campo magnetico y de magnetizacion tienen unidades de $A/m$.

</aside>

# Materiales LIH

Si los materiales son **LIH**, (lineales, isótropos, y homogéneos) entonces podemos encontrar una relación lineal entre los campos mencionados.

$$
\vec M = X_M \cdot \vec H
$$

Siendo $X_M$ la susceptibilidad magnética, un escalar adimensional. $X_M = \mu_r - 1$

Podemos reescribir la relación constitutiva a partir de la expresión anterior

$$
\vec B = \mu_0 \cdot \mu_r \cdot \vec H
$$

Siendo $\mu_r = 1 + X_M$ la permeabilidad relativa. $\mu = \mu_r \cdot \mu_0$

# Materiales Ferromagnéticos

Estos materiales no son lineales, la relación entre el campo magnético y el campo magnetización respeta la curva de Histéresis. Esto se debe a que los materiales tienen memoria y al eliminar el campo magnético, el material sigue magnetizado. 

Sin embargo, vamos a tratar estos materiales como materiales lineales. La permeabilidad relativa de estos materiales es mucho mayor a la del vacío. $\mu_r \gg 1$ 

# Circuitos Magnéticos

Vamos a trabajar con circuitos magnéticos cerrados de materiales ferromagnéticos. Estos circuitos pueden ser toroides tanto circulares como rectangulares, pero van a estar conformados por un solo material magnético, y van a ser enteros. Estos toroides van a tener bobinas que carguen el material.

En estos circuitos, vamos a calcular los tres campos $\vec H, \vec M, \vec B$ dentro del material. 

Tenemos dos tipos de toroides. Los toroides gruesos, son aquellos en los que importa el radio para el calculo del campo magnetico. En los toroides finos, el campo magnético es uniforme.