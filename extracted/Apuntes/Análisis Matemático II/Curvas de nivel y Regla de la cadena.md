# Curvas de nivel y Regla de la cadena

Sea $f: R^2\to R$ diferenciable y $X(x(t), y(t))$ una curva de nivel $k$ de $f$

$$
f(x(t), y(t)) = k\\\underbrace{D_{f\circ X} = 0}_{\text{Buscamos el gradiente de la composicion}}
$$

$$
\boxed{D_f(x(t),y(t)) \cdot\begin{pmatrix}x'(t)\\y'(t)\end{pmatrix} = 0}
$$

El gradiente de una funcion diferenciable de dos variables es en cada punto ortogonal al vector tangente a la curva de nivel que pasa por ese punto

!![[Apuntes/Análisis Matemático II/attachments/Curvas de nivel y Regla de la cadena 2.png]]

---

Sea $f(x,y,z)$ diferenciable, $C_k$ una superficie de nivel. Si tomamos una de las infinitas curvas de nivel $C:(x(t), y(t), z(t))$a

$$
f\circ C(t) = k\\\underbrace{D_{f\circ C} = 0}_{\text{Buscamos el gradiente de la composicion}}
$$

$$
\boxed{\nabla f(x(t),y(t), z(t)) \cdot\begin{pmatrix}x'(t)\\y'(t)\\z'(t)\end{pmatrix} = 0}
$$

El gradiente es perpendicular a las direcciones tangentes a la curva de nivel en ese punto

!![[Apuntes/Análisis Matemático II/attachments/Curvas de nivel y Regla de la cadena 1.png]]