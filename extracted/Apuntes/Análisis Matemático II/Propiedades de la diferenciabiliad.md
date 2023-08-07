# Propiedades de la diferenciabiliad

**Suma de funciones $C^1$ es $C^1$**

**Producto de funcion $C^1$ es $C^1$**

**Cociente de funciones $C^1$ es $C^1$,** (con denominador no nulo) 

# Regla de la Cadena

Sea $\vec f: D\subset\R^n\to\R^m,\vec g: D\subset\R^m\to\R^p$. Si $\vec f$ es diferenciable en $\vec x_0$ y $\vec g$ es diferenciable en $\vec y_0 =\vec f(\vec x_0)$, entonces la composicion $\vec h = \vec g \circ\vec f$, resulta diferenciable en $\vec x_0$. Si existe $\vec h$

$\vec h$ existe si $\text{Img}(f) \subset Dom(g)$

$$
D_{\vec h}(\vec x_0) = D_{\vec g}(\vec f(\vec x_0))\times D_{\vec f}(\vec x_0)
$$

$D_{\vec f}:$ Matriz Jacobiana de $\vec f$

# Arbol de derivacion

!![[Apuntes/Análisis Matemático II/attachments/Propiedades de la diferenciabiliad 1.png]]

$$
h'_x = g'_u f'_x + g'_vf'_x
$$

$$
h'_y = g'_u f'_y + g'_vf'_y
$$

$$
h'_z = g'_u f'_z + g'_vf'_z
$$