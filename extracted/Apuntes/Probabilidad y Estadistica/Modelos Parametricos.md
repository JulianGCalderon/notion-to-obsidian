# Modelos Parametricos

La distribucion de $X$ pertenece a una familia de distribuciones $\mathcal F$ que dependen de un parámetro desconocido

Sera $\mathcal F$ una familia de distribuciones de probabilidad parametrizada por un subconjunto no vacio $M \in \R^p$ llamado espacio parametrico.

$$
\mathcal F = \{ F_\theta(x): \theta \in M\}
$$

# Funcion de Verosimilitud

Llamamos funcion de verosimilitud a la funcion conjunta vista como funcion del parametro desconocido $\theta$

$$
L(\theta) =  \Pi_{i=1}^n f_\theta(x_i)
$$

$$
L(\theta) =  \Pi_{i=1}^n p_\theta(x_i)
$$

<aside>
💡 La letra $L$ viene del ingles “likelihood”

</aside>

# Familia Paramétrica Regular

Diremos que una familia paramétrica es **Regular** si:

1. El soporte de $f_\theta(x)$ no depende de $\theta$
2. $f_\theta(x)$ es derivable con respecto a  $\theta\  \forall x$
3. El conjunto paramétrico $M$ es abierto

# Familias Exponenciales

Se dice que una familia de distribuciones en $\R^q$ con distribucion $F_\theta(x)$ es una familia exponencial a $k$ parametros si su funcion de densidad (o probabilidad) se puede escribir de la siguiente forma

$$
\Large f_\theta(x) = A(\theta) \cdot e^{\sum_{i=1}^k c_i(\theta)r_i(x)} \cdot h(x)
$$

Donde las funciones involucradas:

- $C_i(\theta): M \to \R$
- $A(\theta): M \to \R^+$
- $r_i(x): \R^q \to \R$
- $h_i(x): \R^q \to \R^+$