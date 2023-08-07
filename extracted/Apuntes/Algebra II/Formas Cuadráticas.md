# Formas Cuadráticas

# Definición

Dada una matriz $A \in \R^{n \times n}$ simétrica, una **forma cuadrática en** $\R^n$ es una función $Q: \R^n \to \R$ tal que $Q(x) = x^T Ax$

Las formas cuadráticas se clasifican en positivas, negativas, semi-definidas positivas, semi-definidas negativas, o indefinidas. Segun lo sean las matrices simétricas que las definen.

Si $Q: \R^2 \to \R$, se le llama **Curva de Nivel** $k$ al conjunto $C_k = \{x \in \R^2: Q(x) = k\}$

Si $Q: \R^3 \to \R$, se le llama **Superficie de nivel** $k$ al conjunto $C_k = \{x \in \R^3: Q(x) = k\}$

# Cambio de Variables

Como $A$ es una matriz simétrica, sabemos que es diagonalizable ortogonalmente: $A = PDP^T$, con $D$ una matriz diagonal.

Entonces podremos escribir la forma cuadrática de la siguiente forma

$$
Q(x) = (P^Tx)^T D (P^Tx)
$$

Aplicando un cambio de variables $y^T, y$. Llegamos a la siguiente expresión

$$
Q(y) = y^T D y
$$

Una vez que encuentro los $y$ que necesito, puedo aplicar otro cambio de variables para recuperar $x$

$$
y = P^Tx \iff x = Py
$$

# Teorema de Rayleigh

Este teorema nos permitirá optimizar funciones, encontrando sus máximos y mínimos con restricciones en la norma de $x$.

Tambien podremos encontrar los puntos donde la norma es minima o maxima, dado un conjunto de nivel de la función.

$$
\lambda_\text{min} \cdot \|x\|^2 \leq Q(x) \leq \lambda_\text{max} \cdot \|x\|^2
$$

La igualdad de esta inecuación se cumple en los respectivos subespacios. Es decir, los mínimos y máximos se encuentran en los puntos del auto-espacio asociado a los autovalores mínimos y máximos.

$$
\max_{\|x\|^2 = a^2}Q(x) = a^2 \lambda_{\text{max}} \implies x_\text{max} \in S_{\lambda_\text{max}} \cap \{\|x\|^2 = a^2\}
$$

$$
\min_{\|x\|^2 = a^2}Q(x) = a^2 \lambda_{\text{min}} \implies x_\text{min} \in S_{\lambda_\text{min}} \cap \{\|x\|^2 = a^2\}
$$

Además, sabemos que como $P$ es una matriz ortogonal. $\|x\| = \|y\|$. Por lo que los valores máximos y mínimos de $Q$ serán los mismos incluso después del cambio de variables.

# Restricciones Genéricas

Para optimizar funciones sujetas a una restricción del tipo $R(x) = 1$, Debemos plantear ciertos cambios de variable. $z = B^*x$, Tal que $B^* B^* = B$

$$
\min_{R(x) = 1} Q(x) = \min_{\|z\| = 1} z^T A^* z
$$

Siendo $A^* = B^{*-1} A B^{*-1}$ tal que $B^* B^* = B$

Sin embargo para esto debemos diagonalizar tanto $B$ como $A^*$, Sin embargo podemos simplificar el cálculo mediante la siguiente equivalencia

Los autovalores de $A^*$ son los mismos que $B^{-1}A$. Además, se puede demostrar que si $A^* z = \lambda z$, Entonces $B^{-1}A x = \lambda x$. Por lo que la solución del problema se encuentra encontrando los autovalores y autovectores de $B^{-1}A$. A partir de una equivalencia, llegamos a:

$$
\det(A - \lambda B) = 0
$$

$$
v_i = \text{null}(A - \lambda_1 B)
$$

Por último debemos hallar el vector perteneciente al subespacio de la solución adecuado. Para esto planteamos que $x_{m} = \alpha v_{m}$. Luego $R(x_m) = \alpha^2 R(v_m) = 1$

Si resolvemos para $\alpha$, encontramos los vectores que minimizan la forma cuadrática con la restricción.

<aside>
🔵 Si la restricción es indefinida, entonces la solución no esta a acotada y el mínimo de la forma cuadrática estará asociado al autovalor máximo.

</aside>