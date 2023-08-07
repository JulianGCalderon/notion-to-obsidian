# Bibliotecas Personales

# Header

El compilador los incluye de forma automática al compilar su archivo fuente. Aca se definen las funciones, variables y constantes, que pueden ser accedidas por otro archivo.

Escribo el prototipo de las funciones, y sus pre/post condiciones.

```c
/* aritmetica.h */

#ifndef ARITMETICA_H
#define ARITMETICA_H

// POST: Devuelve la suma de los dos numeros
int sumar(int n1, int n2); // PROTOTIPO DE FUNCION

#endif /* ARITMETICA_H */
```

# Source

Tiene el mismo nombre que el header, pero con extension .c

Aca se definen las funciones de la biblioteca

```c
/* aritmetica.c */

#include "aritmetica.h"

int sumar(int n1, int n2){
	return n1 + n2;
}
```

# Main

En este archivo se encuentra el `main` de la función. Desde aca se accede a las otras bibliotecas

```c
/* main.c */

#include "aritmetica.h"

int main(){
	int suma = sumar(2, 3);
	printf("%i", suma) //5	

	return 0;
}
```

# Terminal

Al momento de compilar, debo incluir solo los archivos fuentes, no los mains

**OPCION 1:**

`gcc -g aritmetica.c -c` → **`aritmetica.o`**

`gcc -g main.c aritmetica.o -o main` → `**main`** 

**OPCION 2:**

`gcc -g main.c aritmetica.c -o main` → `**main**`

Si el procesador encuentra la directiva `#include`, remplaza esta línea por el contenido completo del archivo que se encuentra en el sistema (<> o "")

la directiva `#ifndef` se encarga de que no se definan los elementos del archivo 2 veces, y si ya se definió una vez, entonces omite el archivo.