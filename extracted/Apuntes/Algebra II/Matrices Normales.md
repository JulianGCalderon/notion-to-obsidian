# Matrices Normales

# Clasificación de Matrices

Primero, algunas definiciones sobre matrices:

- **Matrices Simétricas** $\to A^t = A$
- **Matrices Ortogonales** $\to A A^t = A^T A = I$
- **Matrices Anti Simétricas** $\to A^t = -A$
.

Para matrices complejas, tenemos que;

- **Matrices Herméticas** $\to A^* = A$
, Donde $A^*$ representa la matriz adjunta (transpuesta y conjugada)
- **Matrices Unitarias**$\to A A^* = A^* A = I$
- **Matrices Anti Herméticas** $\to A^* = -A$
.

# Matrices Normales

Todas las matrices mencionadas anteriormente pertenecen a un mismo conjunto, el conjunto de las matrices *normales*. Verifican que $A A^* = A^* A$.

## Propiedades: $A, A^*$.

Las siguientes propiedades marcan relaciones entre una matriz y su adjunta:

1. $\lang x, Ay \rang =(Ay)^*x = y^*A^*x = \lang A^*x, y\rang$
2. $\text{Null}(A^*) = \text{Col}^\perp(A)$. Podemos demostrarlo por doble inclusión, y la propiedad $(1)$
3. $\text{Null}^\perp(A^*) = \text{Col}(A)$. Se obtiene de $(2)$, Considerando $\text{Col}^{\perp^\perp}(A) = \text{Col}(A)$
4. $\text{Null}(A) = \text{Col}^\perp(A^*)$. Se obtiene de $(2)$, Intercambiando $A, A^*$
5. $\text{Null}^\perp(A) = \text{Col}(A^*)$. Se obtiene de $(3)$, Intercambiando $A, A^*$

## Matrices Herméticas

Las siguientes propiedades son validas únicamente para matrices herméticas:

- $\lang x, Ay \rang =\lang Ax, y\rang$
- Los autovalores de $A$ son reales
- Los auto espacios correspondientes a autovalores distintos son ortogonales
- Existe una base ortonormal de $\Bbb C^n$ formada por autovectores de $A$. Sus multiplicidades algebraicas y geométricas coinciden. Toda matriz hermética es a su vez, diagonalizable.
    
    <aside>
    💡 Una matriz diagonalizable unitariamente no es necesariamente hermética.
    
    </aside>
    

**Matrices Definidas Positivas:** 

Una matriz $A$ es definida positiva si $A^* = A$, y $x^* Ax > 0$, para todo $x$ no nulo.

Estas matrices tienen todos sus autovalores positivos (y reales)

**Matrices Semi Definidas Positiva:** 

Una matriz $A$ es definida negativa si $A^* = A$, y $x^* Ax \geq 0$, para todo $x$ no nulo.

Estas matrices tienen todos sus autovalores no negativos (y reales)

**Matrices Indefinidas** 

Estas matrices tienen autovalores tanto positivos como negativos (reales)

## Matrices Unitarias

Las siguientes propiedades son validas únicamente para matrices unitarias:

- Sus autovalores tienen modulo $1$.
- El determinante tiene modulo $1$. (El determinante es el producto de sus autovalores)
- Sean $U,V$ dos matrices unitarias, $UV$ es unitaria.
- $\lang Ux, Uy \rang = \lang x, y\rang$. La multiplicación por una matriz unitaria preserva el producto interno.
- $\|Ux\| = \|x\|$. La multiplicación por una matriz unitaria preserva la norma.
- Los autovectores de una matriz unitaria asociados a autovalores distintos son ortogonales.
- Las matrices unitarias son inversibles, se cumple que $U^{-1} = U^*$

## Matrices Simetricas

Las matrices simétricas son diagonalizable ortogonalmente. Además, son las únicas matrices reales diagonalizables ortogonalmente.

## Matrices Anti Herméticas

Las siguientes propiedades son validas únicamente para matrices anti herméticas (y anti simétricas):

- Para todo $x \in \Bbb C^n$, $x^* A x$ es imaginario puro o nulo
- Los autovalores de $A$ son imaginarios puros o nulos.
- Los autovectores asociados a autovalores distintos son ortogonales
- Existe $U$ unitaria tal que $A = U DU^{-1}$

# Isometrías

Sea $\Bbb V$ un espacio vectorial con producto interno, entonces el operador $T: \Bbb V \to \Bbb V$ es una ***isometría*** si

$$
d(T(x), T(y)) = d(x,y)
$$

$$
\|T(x)\| = \|x\|
$$

Es decir, el operador $T$ preserva la norma. Además, preserva el producto interno.

El producto interno se preserva si y solo si se preserva la norma.