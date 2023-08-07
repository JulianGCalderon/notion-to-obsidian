# Polinomio de Taylor

El teorema de Taylor permite obtener aproximaciones polinomicas de una funcion de un entorno de cierto punto en el que la funcion sea diferenciable.

Para realizar esta aproximacion, se igualan las derivadas de la funcion original a las derivadas de la aproximacion polinomica

$$
P(a) = f(a),\quad P'(a) = f'(a) ,\quad P''(a) = f''(a),\quad \cdots
$$

$$
P(x) = a_0 + a_1(x-a) + a_2(x-a)^2 + \cdots
$$

De esta manera, podemos definir el polinimio de taylor como:

$$
P(x) = \overbrace{\underbrace{f(a) + \frac{df}{dx}\frac{\cdot(x-a)^1}{1!}}_{\text{Aproximacion Lineal}}+\frac{d^2f}{dx^2}\frac{\cdot(x-a)^2}{2!}}^{\text{Aproximacion Cuadratica}} + \cdots
$$

El polinimio de taylor de grado $n$ es igual al polinimio de grado $(n-1)$ $+$ un termino de grado $n$

$$
P_n(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!}\cdot(x-a)^k
$$

$$
P_{n+1}(x) = P_n(x) + \frac{f^{(n+1)}}{(n+1)!}\cdot(x-a)^{n+1}
$$

# Polinomios de Taylor en varias variables

En campos escalares, se debe comprobar que todas las derivadas parciales del polinomio tengan el mismo valor que las derivadas parciales de $f$.

De esta manera, se demuestra que, para un polinomio de taylor de grado 2,

$$
\begin{align*}p(x_0, y_0) &= f(x_0, y_0)\\p'_x(x_0, y_0) &= f'_x(x_0, y_0)\\p'_y(x_0, y_0) &= f'_y(x_0, y_0)\\p''_{xx}(x_0, y_0) &= f''_{xx}(x_0, y_0)\\p''_{xy}(x_0, y_0) &= f''_{xy}(x_0, y_0)\\p''_{yy}(x_0, y_0) &= f''_{yy}(x_0, y_0)\\\end{align*}
$$

Asi resulta el unico polinomio de taylor de grado 2 en $x,y$ es:

$$
\begin{align*}p_2(&x_0, y_0) = \overbrace{f(x_0, y_0) + f'_x(x_0, y_0)(x-x_0) + f'y(x_0, y_0)(y-y_0)}^\text{Aproximacion Lineal (Plano Tangente)}+\\ &+ \frac{1}{2!}\bigg[ f''_{xx}(x_0, y_0)(x-x_0)^2 + 2f''_{xy}(x_0, y_0)(x-x_0)(y-y_0) + f''_{yy}(x_0, y_0)(y-y_0)^2\bigg]\end{align*}
$$

---

Analogamente, el polinomio de taylor de grado 3 en $x,y$ es:

$$
\begin{align*}p_3&(x_0, y_0) = p_2(x_0, y_0)\\+&\frac{1}{3!}\bigg[f'''_{xxx}(x_0, y_0)(x-x_0)^3 + f'''_{yyy}(x_0, y_0)(y-y_0)^3\\&+3f'''_{xxy}(x_0, y_0)(x-x_0)^2(y-y_0)\\&+3f'''_{yyx}(x_0, y_0)(x-x_0)(y-y_0)^2\bigg]\end{align*}
$$

## Definicion Formal

$$
p_k(x,y) = f(x_0, y_0) + \sum_{i=0}^k\frac{1}{i!}\sum_{j=0}^i\binom ij\frac{\partial^if}{\partial x^{i-j}\partial y^j}(x_0, y_0)(x-x_0)^{i-j}(y-y_0)^j
$$