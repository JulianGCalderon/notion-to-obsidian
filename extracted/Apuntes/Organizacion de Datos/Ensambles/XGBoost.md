# XGBoost

Fue diseñado para ser trabajado en *big data*, adaptado para volúmenes grandes de datos.

1. Realizamos una predicción inicial (por defecto 0.5)
2. Calculamos los residuos de las observaciones
3. Construimos un árbol para los residuos, colocando los residuos en una sola hoja.
4. Calculamos el *Similarity Score* para los residuos: ($\lambda$ se utiliza para disminuir la varianza). Inicialmente $\lambda = 0$

$$
\text{SS} = \frac{(\text{Suma de Residuos})^2}{\text{Cantidad de Residuos} + \lambda}
$$

<aside>
💡 **Ridge Regression** es una variación de la regresión lineal que busca encontrar una recta *no tan buena* para predecir, introducimos un sesgo que permita perder la varianza. Obtendremos una predicción peor para los datos de entrenamiento.

</aside>

1. Buscamos el siguiente nodo, para ello calculamos la ganancia total. Tomamos como umbral la distancia entre un par de observaciones y seleccionamos el par con mayor ganancia..
    
    $$
    \text{G} = SS_{\text{izquierda}} + SS_{\text{derecha }}+ SS_{\text{raiz}} 
    $$
    
2. Repetimos el algoritmo anterior hasta llegar a la profundidad deseada
3. Realizamos una poda: Elegimos un número al azar llamado $\gamma$. Calculamos la diferencia entre el $G$ del nodo más bajo y $\gamma$. Si la diferencia es negativa, removemos el nodo. Solo nos quedamos con aquellos nodos cuya ganancia es mayor a nuestro umbral de poda.

Si volvemos a calcular el árbol, pero con $\lambda = 1$. Es más probable la poda del árbol. Este previene el sobreajuste del modelo. Al igual que el método anterior, tendremos un *learning rate* para disminuir la varianza.

Este algoritmo se repite hasta alcanzar un número de árboles límite, o un residuo mínimo.