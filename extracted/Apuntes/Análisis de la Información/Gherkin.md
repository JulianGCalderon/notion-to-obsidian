# Gherkin

# ¿Que es BDD?

Nace dentro de las metodologías ágiles de software. Busca alentar la colaboración conjunta entre distintas partes interesadas en el proyecto.

Busca establecer un lenguaje dentro del dominio (DSL) usando construcciones naturales al humano las cuales expresan comportamiento. Combina técnicas de TDD y DDD.

La idea es que todos puedan entender lo que se define en un comportamiento, usando palabras no técnicas.

# Gherkin

*Gherkin* es un lenguaje que permite definir estos comportamientos (******behaviour****** *********************and expected outcomes).********************* Junto a *Cucumber*, podemos definir pruebas automatizadas para *Java*.

Las pruebas de *******Gherkin******* deben tener el siguiente formato.

!![[Apuntes/Análisis de la Información/attachments/Gherkin 1.png]]

A partir de ********Cucumber********, esto se transformara en código el cual verificará el funcionamiento de nuestro programa.

Una vez obtenidas las pruebas, podemos realizar TDD para implementar lo necesario para cumplir el comportamiento esperado.