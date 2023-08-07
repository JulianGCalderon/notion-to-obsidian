# Producto Interno

# Definicion

Si $\Bbb V$ es un $\Bbb K$-espacio vectorial, se dice que una función $\lang *,* \rang: \Bbb V \times \Bbb V \to \Bbb K$ es un producto interno **(P.I.)**, si cumple:

- $\lang \alpha u + \beta v, w\rang = \alpha \lang u, w\rang + \beta \lang v, w\rang
\impliedby \forall u,v,w \in \Bbb V \ \land\  \forall \alpha, \beta \in \Bbb K$
- $\lang u,v\rang = \overline{\lang v,u\rang } \impliedby \forall u,v \in V$ **(Conjugado)**
- $\lang u,u\rang > 0 \iff u \in \Bbb V \neq 0_V$
- $\lang u,u\rang = 0 \iff u \in \Bbb V = 0_V$

## Consecuencias Inmediatas

1. $\lang u,u\rang \in \R \impliedby \forall u \in \Bbb V$
2. $\lang u, \alpha v + \beta w\rang = \overline{\alpha}\lang u,v\rang + \overline{\beta}\lang u,w\rang \impliedby \forall u,v,w \in \Bbb V$
3. $\lang0,u\rang = 0 \impliedby \forall u \in \Bbb V$

## Nociones del Producto Interno

**Norma:** (inducida por el producto interno)

$$
\|u\| = \sqrt{\lang u,u\rang}
$$

Cumple las siguiente propiedades:

- $||u|| > 0$
- $||\lambda u|| = |\lambda|.||u||$
- $|| u || = 0 \iff u = 0_V$

**Distancia:** Sean $u,v \in \Bbb V$, definimos la distancia entre $u,v$ como

$$
d(u,v) = \|u - v\| = \|v - u\|
$$

**Ortogonalidad:** Sean $u, v \in \Bbb V$, se dice que son ortogonales si

$$
\lang u,v \rang = 0 \iff u \perp v
$$

## Ejemplos Básicos

- **Producto Interno canónico en $\R^n$,** Se cumple la siguiente igualdad para $X, Y \in \R^n$
    
    $$
    \lang X,Y\rang = Y^TX
    $$
    
- **Producto Interno canónico en $C^n$,** Se cumple la siguiente igualdad para $X, Y \in \Bbb C^n$
    
    $$
    \lang X, Y\rang = \overline{Y}^TX
    $$
    
- Si tomamos $\Bbb V$ = $C([0,1])$, entonces para $f, g$  funciones continuas en el intervalo $[0,1]$
    
    $$
    \lang f,g \rang  = \int_0^1 f(t)g(t)dt
    $$
    
    <aside>
    💡 Este producto interno nos permite calcular la norma y la distancia entre funciones continuas.
    
    </aside>
    

- Si tomamos $\Bbb V = \R^2$, entonces para $X, Y \in \Bbb V$, podemos definir el producto interno
    
    $$
    \lang X,Y\rang = X\begin{pmatrix} 4 & -1 \\ -1 & 2\end{pmatrix} Y^T
    $$
    
    Lo que es equivalente a la siguiente expresión
    
    $$
    \lang (x_1,x_2)^T, (y_1,y_2)^T\rang = (x_1, x_2)\begin{pmatrix} 4 & -1 \\ -1 & 2\end{pmatrix}\begin{pmatrix}y_1 \\ y_2\end{pmatrix}
    
    \\
    
    \lang (x_1,x_2)^T, (y_1,y_2)^T\rang = (4x_1y_1 -x_2y_1 -x_1y_2+ 2x_2y_2)
    $$
    

# Base de Producto Interno

Si $\Bbb V$ es un espacio vectorial de dimensión finita, todo **P.I.** queda definido sobre una base de $\Bbb V$. Más aún, si $B = \{v_1,...,v_n\}$ todo **P.I**. puede escribirse como:

$$
\lang u,v\rang = \overline{[v]^B}^T G_B[u]^B = [u]^{B^T}G_B\overline{[v]^B}
$$

$$
\lang u, v\rang = [x_1,x_2,...,x_n]
\begin{bmatrix}

\lang v_1, v_1\rang & \lang v_1, v_2\rang & \cdots &  \lang v_1, v_n\rang \\  \lang v_2, v_1\rang &  \lang v_2, v_2\rang & \cdots &  \lang v_2, v_n\rang \\ \vdots & \vdots & \ddots & \vdots \\  \lang v_n, v_1\rang &  \lang v_n, v_2\rang & \cdots &  \lang v_n, v_n\rang

\end{bmatrix}

\begin{bmatrix}\overline{y_1} \\ \overline{y_2} \\ \vdots \\ \overline{y_n}\end{bmatrix}
$$

Con $G_B \in K^{n\times n}$ una matriz hermética y definida positiva.

- $G_B \in K^{n\times n}$ es una matriz **hermética** si y solo si $G_B = \overline{G_B}^T$, Las matrices hermética son un subconjunto de las matrices simétricas, extendida a las matrices con coeficientes reales.
- $G_B \in K^{n\times n}$ es definida **positiva** si y solo si $X^TG_BX > 0 \impliedby \forall X \in K^n \neq \{0_{\Bbb K^n}\}$

# Propiedades

**Desigualdad de Cauchy-Bunyakovsky-Schwarz:**

$$
| \lang u,v \rang | \leq \|u\| \|v\| \impliedby \forall u,v \in \Bbb V
$$

$$
\text{Mas aun:}

\begin{cases}

| \lang u,v \rang | = \|u\| \|v\| \iff u,v \text{ son L.D} \\

| \lang u,v \rang | < \|u\| \|v\| \iff u,v \text{ son L.I} \\

\end{cases}
$$

**Desigualdad Triangular:**

$$
\|u + v\| \leq \|u\| + \|v\| \impliedby \forall u,c \in \Bbb V
$$

**Teorema de Pitágoras:** 

Si $\lang u,v \rang = 0 \iff u \perp v$ (es decir, si trabajamos con vectores perpendiculares) se cumple que

$$
\|u + v\|^2 = \|u\|^2 + \|v\|^2
$$

**Angulo entre** $u, v$:

Como consecuencia la desigualdad de *Cauchy-Bunyakovsky-Schwarz* , llegamos a la siguiente expresión

$$
-1 \leq \frac{\lang u,v \rang}{\|u\| \|v\|}\leq 1
$$

Extendemos entonces la definición de ángulo, para cualquier $\R$-espacio vectorial

$$
\cos(\theta) = \frac{\lang u,v \rang}{\|u\| \|v\|} \impliedby \theta \in [0, \pi]
$$

$$
\alpha(u,v) = \theta
$$

**Area de un triangulo**

Sea $\triangle$ un triangulo de vertices $(0, e_1, e_2)$, entonces el area de este triangulo se calcula con la siguiente formula

$$
A(\triangle) = \frac 12 \cdot \sqrt{\|e_1\|^2\|e_2\|^2 - \lang e_1, e_2\rang^2}
$$