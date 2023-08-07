# Grafos Particulares

- $N_n:$ Grafo nulo de orden $n$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 16.png]]
    
- $K_n:$ Grafo simple completo de orden $n$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 1.png]]
    
- $P_n:$ Camino simple de longitud $n$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 8.png]]
    
- $C_n:$ Ciclo de longitud $n$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 9.png]]
    
- $S_n:$ Estrella. Grafo simple conexo de $n$ vertices con un único vértice de grado $n-1$ que se conecta con los $n{-}1$ restantes vertices de grado $1$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 10.png]]
    
- $W_n:$ Rueda. Puede pensarse coloquialmente como una estrella y un ciclo en los satélites.
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 11.png]]
    
- $\text{Peon}$: Este es un grafo común, utilizado para demostrar muchas propiedades:

!![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 12.png]]

- $2p$-**************Corona:************** Una $2p$-corona es un bipartito $G(U, V)$ tal que $u_iv_j \in E(G) \iff i\neq j$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 13.png]]
    
    Este grafo sera bipartito por su propia definición, pero no sera completo (podemos observarlo en la figura
    
- $p$-************Book:************ Definido como $p$ ciclos $C_4$ todos compartiendo una arista en común. Puede ser definida a partir de operaciones, como $B(p) = S_{p+1} \times P_2$.
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 14.png]]
    
    Los libros son bipartitos ya que las estrellas lo son, y los vertices de cada estrella solo son adyacentes a sus análogos en la segunda estrella. De esta forma, se pueden colorear inversamente las estrellas, formando un grafo bipartito
    
- $**p$-Cube:** Grafo con $2^p$ vertices. Los vertices se etiquetan con una cadena binaria de $p$ digitos, con una arista si la distancia *******hamming******* es 1. Alternativamente, puede pensarse con el producto cartesiano de $p$ veces $K_2$
    
    La distancia *******hamming******* entre dos cadenas indica la cantidad de ****bits**** distintos
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 15.png]]
    
- $W_d(p,q):$ Se define como un molino de $q$ aspas de longitud $p-1$, puede formarse con el ensamble  $W_d(p,q) = N_1 * qK_{p-1}$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 2.png]]
    
- $F(p,q):$ El abanico se define por $F(p,q) = N_p * P_q$
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 3.png]]
    
- $L_{p,q}:$ ******************Lollipop.****************** Es el grafo simple compuesto por el $K_p$ y el grafo $P_q$ conectados por un puente
- $T_{p,q}:$ ********************Renacuajo.******************** Es el grafo simple resultante de conectar $C_p$ con $P_q$ mediante un puente
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 4.png]]
    
    *Chupetín* a la izquierda, y Renacuajo a la derecha
    
- $KP(p,q,l):$ **********Remo.********** Es el grafo simple resultante de unir el ciclo $C_p$ con el ciclo $C_q$ mediante un ****path**** de longitud $l$.
- $B_p:$ ********Pesa********. Es el grafo simple obtenido de conectar dos copias de $k_p$ con un puente
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 5.png]]
    
    El tamaño del ****path**** en los últimos cuatro grafos es referido según su longitud, y no la cantidad de sus nodos 
    
- $K(p,q):$ ****************************Grafo de *Kneser.** Dado un* $p$-conjunto $H$ fijo, se define el grafo simple $G = K(p,q)$ siendo $V(G)$ = $\mathcal{P}_q(H)$ (los $q$-subconjuntos de $H$) con $uv \in E(G)$ ***sii*** $uv = \empty$. Es decir, dos vertices son adyacentes ***sii*** los correspondientes conjuntos son disjuntos. Genéricamente, definimos $K(p,q,s)$ donde $uv \in E(G)$ ****sii**** $|uv| \leq s$, y entonces particularmente $K(p,q) = K(p,q,0)$.
    
    El miembro ilustre de la familia $K(5,2)$ es isomorfo al grafo de *Petersen.*
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 6.png]]
    
    Denotamos $ij$ al vector asociado al conjunto ${i, j}$
    
    Genéricamente, podemos hallar el tamaño del grafo de ******Kneser****** a partir de la cantidad de formas posibles de tomar $q$ elementos de un conjunto de $p$ elementos, es decir, el numero combinatorio
    
    $$
    n(K(p,q)) = \binom{p}{q}
    $$
    
    Para las aristas, cada vértice sera adyacente a aquellos nodos con los cuales no comparta elementos, luego esto es el numero combinatorio $\binom{p-q}{q}$, Como cada arista se contara dos veces, dividimos el numero en dos. Tendremos entonces
    
    $$
    m(K(p,q)) = \frac 12 \binom pq \binom {p-q}q
    $$
    
    Si $q > p$, entonces el grafo sera vacío, que es un grafo en si mismo. La función del grafo vacío se denomina función nula.
    
    Por otro lado, si $p - q < q$, entonces el grafo no tendrá aristas..
    
- $J(p,q):$ **********************************Grafo de Johnson.********************************** Dado un $p$-conjunto $H$ fijo, se define el grafo simple $G = J(p,q)$ con $q \geq 1$, donde $V(G) = \mathcal P_q(H)$ y $uv \in E(G)$ ***sii*** $|uv| = q-1$. Es decir, dos vertices son adyacentes ***sii*** la intersección de los conjuntos asociados es de cardinalidad $q-1$. Algunas relaciones particulares son $J(p, 1) \cong J(p, p-1) \cong K_p$. El grafo de J*******ohnson******* generalizo se define como $J(p,q,r)$ donde dos vertices son adyacentes si $|uv| = r$.
    
    !![[Apuntes/Matemática Discreta/attachments/Grafos Particulares 7.png]]
    
    Al igual que con el grafo de ******Kneser******, calcularemos el tamaño del grafo a partir del numero combinatorio $\binom pq$.
    
    Para calcular el grado de cada nodo, sabemos que por cada elemento del conjunto asociado, podremos conectarnos con los nodos cuyo conjunto asociado difieran en únicamente ese elemento. Como difieren en únicamente ese elemento, este no debe pertenecer al propio nodo, luego $d(v) = q(p-q)$. El cardinal del grafo entonces será:
    
    $$
    m(J(p,q)) = \frac 12 \binom pq q(p-q)
    $$