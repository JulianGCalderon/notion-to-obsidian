# Punto Flotante

Cuando queremos mas precision a la hora de representar números decimales, podemos utilizar el sistema de representación de punto flotante. Utiliza la notación científica para representar números.

$$
M \cdot \text{base}^{exp}
$$

Por norma, se usa la base binaria para representar el numero.

El principal inconveniente del punto flotante, es que el cero y los valores cercanos a el no pueden ser representados. El cero se representa con un valor especial. 

# Componentes

- **Signo:** Representa el signo del numero.
- **Mantisa:** Representa el significado del numero. Por norma, empieza con $1,d_1d_2d_3 \dots d_n$
- **Exponente:** Representa la magnitud del numero (con signo). Se representa con *“exceso”.* En el exponente no están permitidos los extremos del rango de representación. No admite todos ceros ni todos unos.

!![[Apuntes/Análisis Numérico/attachments/Punto Flotante 1.png]]

Formatos típicos de los números de maquina.

## Representación en Exceso

Si se tienen 4 bits, Parte del -7 con todos los bits en 0. Luego va sumando uno por uno hasta llegar al 7 positivo. El numero inicial depende de la cantidad de bits del numero.

La ventaja de este sistema de representación es que es mas fácil comprar exponentes. 

# Valores Especiales

- **Cero:** Todos los bits en cero. (no importa el signo)
- **Infinito:** Exponente: Todos unos, Mantisa: Todos ceros. (no importa el signo)
- **NaN**: Exponente: Todos unos, Mantisa: ≠ 0  (no importa el signo)

# Sumar en Punto Flotante

Esta operación es muy costosa, mucho menos efectiva que en punto fijo.

1. Calcular la diferencia $d$ de exponentes (cual es mayor)
2. Correr $d$ posiciones a la derecha la coma del numero mayor
3. Sumar las mantisas
4. El exponente del resultado es el del numero mayor
5. Normalizar la mantisa, ajustando el exponente de ser necesario.