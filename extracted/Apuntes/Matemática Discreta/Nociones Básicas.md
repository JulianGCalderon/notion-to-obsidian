# Nociones Básicas

# Definición

Definimos un grafo $G = (V(G), E(G), \Psi_G)$ como una terna de un conjunto de vertices $V(G)$, un conjunto de aristas $E(G)$ y una función $\Psi_G$ que relaciona los vertices con las aristas.

- Definimos el orden del grafo $n(G) = |V(G)|$
- Definimos el tamaño de un grafo $m(G) = |E(G)|$

El grafo se puede denominar según su tamaño y orden, de la forma $G(n,m)$

# Aristas

Generalmente, definimos la función de incidencia:

$$
 ⁍
$$

Para definir $\Psi_G$ utilizamos alguna de las siguientes notaciones:

$$
\Psi_G(e_1) = \{v_1, v_2\}
$$

$$
\Psi_G(e_1) = v_1v_2
$$

$$
e_1 = v_1v_2
$$

- Las aristas que que inciden dos veces en el mismo vértice se denominan **lazos**
- Si hay dos aristas que inciden sobre los mismos dos vertices, entonces estas aristas son **multiples**

El entorno abierto de un vértice es el conjunto de vertices que se conectan con el directamente, y se define

$$
 ⁍
$$

El entorno cerrado es aquel que incluye al camino trivial propio

$$
\Gamma[v] = \Gamma(v) \cup \{v\}
$$

Un grafo es simple si no tiene lazos ni aristas multiples. En los grafos simples puede prescindirse de etiquetas en las aristas porque sus extremos las definen inequívocamente.

# Grado de Vértice

El grado de un vértice $d(v)$, del ingles ******degree****** es la cantidad de aristas que inciden sobre ese vértice. La sucesión de grados $d(G)$ es un vector no decreciente con el grado de cada uno de los vertices.

- Definimos $\delta(G)$ como el grado mínimo del grafo.
- Definimos $\Delta(G)$ como el grado máximo del grafo.
- También denotamos $\overline d(G)$ como el grado promedio del grafo

Si todos los vértices de un grafo tienen el mismo grado, se dice que es regular

Si todos los vertices del grafo $G$ tienen de grado $\delta(G)$, excepto uno de grado $\Delta(G) = \delta(G) + 1$, entonces se dice que es un grafo casi regular.

## Sucesión Grafica

Se dice que la sucesión $P=(p_1, p_2, \cdots, p_n)$ es grafica si existe un grafo $G(n,m)$ cuya sucesión de grafos es $P$.

****************Teorema:**************** Si $P$ es una sucesión de naturales cuya suma es par, entones siempre es una sucesión grafica de algún grafo, posiblemente simple.

**Algoritmo de Construcción de Grafo:** 

1. Unir todos los vertices de grado impar, siempre podre ya que hay una cantidad par de ellos
2. Coloco una cantidad de lazos igual al grado de cada vértice restante (este será par) partido por dos.
3. Se formó un grafo no simple con la sucesión dada.

# Formas Matriciales

Se define $A_g$ a la matriz de adyacencia de $G$ tal que $A_g(i,j)$ es la cantidad de aristas que conectan el vértice $v_i$ con el vértice $v_j$. Los lazos cuentan doble.

Se define $M_g$ a la matriz de incidencias de $G$ tal que $A_g(i,j)$ lleva un uno si la arista $j$ incide en $i$, y lleva un dos si es un lazo. 

Podemos probar por inducción que $A_G^q(i,j)$ cuenta la cantidad de caminos de longitud $q$ entre $v_i$ y $v_j$.

Por otro lado, a partir de la definición, tendremos que $M_GM_G^T = A_G + D$, con $D$ la matriz diagonal de los grados de los vertices del grafo.

# Complemento de un Grafo Simple

Sea $G$ un grafo simple, entonces definimos su complemento como $G'$, donde:

- $V(G') = V(G)$
- $e \in E(G’) \iff e \notin E(G)$

Observamos que si sumamos $d(G) + d(G')$, obtendremos una sucesión estable, como si fuera la del grafo $K_n$.

# Espectro de un Grafo

Sea $G$ un grafo, entonces definimos su espectro $\sigma(G)$ como el espectro de su matriz de adyacencia, $\sigma(A_G)$.

El espectro de un grafo es un invariante, pero no lo caracteriza. Dos grafos no isomorfos pueden tener el mismo espectro (aunque no es tan fácil de encontrar)

Un $C_4 + N_1$ tiene el mismo espectro que un $K_{4,1}$, pero no son isomorfos. Trivialmente, uno es conexo y el otro no.

Notemos que la matriz de adyacencia depende del etiquetado de sus vertices, sin embargo, el espectro no depende de el. Sean $A, B$ dos matrices de adyacencia para dos grafos $G, H$ isomorfos. Entonces las matrices $A, B$ son semejantes (la misma permutación de vertices que define el isomorfismo, puede definir el cambio de las matrices).  Si dos matrices son semejantes, comparten el mismo espectro. Ademas, una matriz simétrica es semejante a su matriz diagonal. 

$$
G \sim H \iff A_G \sim A_H
$$

La suma de autovalores de la matriz de adyacencia sera, por ser cuadrada, la traza de la misma.

$$
\sum_{k=1}^n \lambda_k = 0
$$

Recordemos también que sea $p$ un polinomio y $P$, su polinomio de matrices asociado, entonces si $\lambda$ es autovalor de $A$, $p(\lambda)$ es autovalor de $P(A)$. Esto implica que si $\lambda$ es autovalor de $A$, $\lambda^n$ es autovalor de $A^n$. 

Luego, la suma de los autovalores de $A^2$ es la suma de ciclos de longitud dos, cada uno contado dos veces.

$$
\sum_{k=1}^n \lambda_k^2 = 2m
$$

De igual forma, la suma de los autovalores de $A^3$ es la suma de triángulos, cada uno se cuenta tres veces (una por cada vértice), y cada uno tiene dos orientaciones, luego cada uno se cuenta 6 veces, entonces sea $\tau$ la cantidad de triángulos en $G$

$$
\sum_{k=1}^n \lambda_k^3 = 6\tau
$$

La matriz $J$, completa con unos, tiene $n-1$ autovalores de valor $0$, y un solo autovalor de multiplicidad de valor $n$. A partir de estas definiciones, podremos definir el espectro de $K_n$. Su matriz de adyacencia sera $J - I$, luego definimos el polinomio $p(\lambda) = \lambda -1$, y su polinomio matricial asociado $P(A) = A - I$. Entonces, $A_{K_n} = J - I = P(J)$. Luego, el espectro de $K_n$ será $\sigma(G) = \{-1\ (\text{orden }n-1), n-1\}$.

De forma similar, se demuestra que el espectro de un bipartito $K_{r,s}$ será $\sigma(G) = \{\pm\sqrt{rs}, 0 (r+s - 2)\}$. El espectro de un ****path**** $P_n$ será $\sigma(G) = \{2\cos(k\pi/(n+1)), k = 1,2,\cdots, n\}$. El espectro de un cubo $Q_3$, será $\sigma(G) = \{-3, 3, 1(3), -1(3)\}$.