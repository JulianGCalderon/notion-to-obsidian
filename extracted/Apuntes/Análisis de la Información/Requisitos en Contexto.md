# Requisitos en Contexto

Las técnicas de ingeniería de requisitos dependerán totalmente de el contexto de la aplicación a desarrollar.

Las organizaciones usualmente tienen un plan estratégico basado en lo que perciben que busca el mercado. Decide el objetivo y como se va a tratar de alcanzar. Esta estrategia se utilizara para generar ideas y oportunidades. Los clientes serán generadores de nuevas ideas y oportunidades.

Adicionalmente, con la estrategia determinaremos como gestionamos la cartera de proyectos y la cartera de productos y servicios. Los productos a su vez, alimentan las nuevas ideas.

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 9.png]]

Las ideas no siempre se transforman en productos. Debemos saber si las ideas son factibles antes de realizar una ingeniería de requisitos completas o un análisis muy detallado. Debemos realizar un análisis de factibilidad, de orden de magnitud.

# ¿Que hacemos en un Startup?

Muchas veces, no sabemos que quieren los clientes. Se dan dos situaciones en paralelo:

- Desarrollo de productos
- Desarrollo de clientes

Investigamos que producto podemos desarrollar, creamos un ***MVP***, obtenemos ********feedback******** de nuestros clientes.

Este tipo de desarrollo es mucho mas dinámico, ya que debemos descubrir nuestro público a medida que desarrollamos.

Es mas dinámico, hay mas lugar a la innovación

# Requisitos en el Ciclo de Vida

Los requisitos no están aislados. Son la fuente para el desarrollo del producto, para definir su visión, los riesgos, la arquitectura. Cuando hablamos de trazabilidad, estamos buscando el vinculo entre los requisitos y el resto de elementos del desarrollo del software.

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 1.png]]

Sirven para en buena medida, realizar una estimación de esfuerzo. ¿Cuanto trabajo nos tomara el producto?. Debemos realizar una estimación del tamaño del proyecto a desarrollar. A partir del tamaño, podemos estimar el esfuerzo y a su vez, la duración del proyecto. Del esfuerzo, también podemos estimar los recursos que necesitaremos y los costos asociados

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 2.png]]

# Método de Estimación

Existen dos grupos principales en los métodos de estimación:

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 3.png]]

Métodos algorítmicos:

- Los *Cocomo/Cocomo II* parten de una estimación previo de la cantidad de líneas de código que se necesitaran. En función de eso, se busca determinar la cantidad de horas del proyecto.
- La técnica de puntos función busca determinar también el tamaño a partir de una definición abstracta del sistema (como los casos de uso o las historias de usuario).
- Los use case points plantean algo parecido

Métodos no algorítmicos:

- Story Points: Muy ligados al desarrollo ágil. Es una técnica abstracta que nos muestra la complejidad relativa de cada item del producto backlog. El grupo de trabajo determinara la dificultad de implementación de cada item. El equipo estima en conjunto y los participantes dan su estimación en simultaneo para evitar influenciar a los demás. Una técnica muy usual es el planning poker.

# Requisitos en Distintos Escenarios

Cada situación requiere un enfoque distinto, cada uno tiene sus propias problemáticas y dificultades: Algunos posibles escenarios son:

- Desarrollo ágil
- Evolución de un producto existente
- Migración de un sistema a otro
- Tercerización de un servicio
- Paquetes/SaaS

# Requisitos en Desarrollo Ágil

## Proceso Unificado y Variantes

Los requisitos suceden con diverso grado de intensidad dependiendo de la fase. En las primeras fases del proyecto hay mucho análisis de requisito, y luego va disminuyendo gradualmente, pero nunca finaliza.

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 4.png]]

Durante la fase inicial se busca tener un pantallazo general e indagar en un porcentaje pequeño de los requisitos de mayor riesgo.

## Extreme Programming

Una de las primeras metodologías agiles. Plantea un enfoque de desarrollo iterativo con programación de a pares e integración frecuente.

Se trabaja mucho sobre las historias de usuario y la definición de los casos de prueba.

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 5.png]]

No hay actividades formales ni requisitos escritos. El eje se trata en programar y liberar frecuentemente. Funciona mejor con equipos pequeños y de alta experiencia.

## Scrum

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 6.png]]

Se parte de una visión para generar un ***************product backlog***************. Que detalle las funcionalidades del sistema. Se elabora un **************sprint backlog************** con un subconjunto del product backlog que se van a desarrollar en el release. El sprint dura de 2 a 4 semanas, con reuniones diarias. Al final del ******sprint******, debería tener un producto potencialmente entregable.

Usualmente, los requisitos se organizan en ********user story mapping******** y **********user stories**********. Estos son recordatorios de reuniones con los clientes. De ser necesaria mas información, se pueden utilizar documentación complementaria.

El backlog se define constantemente a medida que se conoce mas acerca del producto y sus requerimientos.

## FDD

Se desarrolla un modelo inicial a partir de la idea del producto, y una lista de ********features******** a desarrollar. Luego se organiza en iteraciones que toman una pequeña porción de la lista de ********features********. A diferencia de otras técnicas, habla de la importancia de diseñar modelos del ********software********.

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 7.png]]

Tiene una estructura jerárquica para organizar las características a implementar.

## DAD

Toma ideas del proceso unificado. Hay una fase de inspection, otra de construction, y otra de transition (desaparece elaboration). El desarrollo es similar a *****scrum*****.

Cuando finaliza una iteración, se refina el **************product backlog**************. Cuando termino de iterar, llego al final de la fase de construcción y comienza la producción.

Se sugiere el uso de *historias de usuario* para describir los requisitos*.*

# Requisitos en Evolución de Sistemas

Algunos problemas que suelen surgir son:

- Los desarrolladores originales ya no están disponibles
- Falta documentación. El conocimiento de la aplicación es implícito, esta en los desarrolladores originales
- Hay resistencia de los usuarios a las nuevas funcionalidades
- Impacto en funcionalidad existente y performance
- 

Es muy importante entender ******que****** hace el sistema con el cual debemos trabajar. Para esto, podemos:

- Crear un árbol de funcionalidades.
- Identificar clases de usuario
- Entender procesos de negocio
- Documentar reglas de negocio (no siempre están escritas, a veces están únicamente implementadas)
- Crear casos de uso o historias de usuario de alto nivel
- Crear diagramas de contexto de alto nivel
- Crear un diagrama de dialogo
- Crear un modelo de datos
- Desarrollar prototipos
- Inspeccionar requisitos

# Requisitos en Migración de Sistemas

Implica tomar un sistema que esta funcionando, y replicarlo en un nuevo sistema con los mismos requisitos. Debemos analizar si debemos eliminar algunos requisitos, cambiarlos, o crear nuevos. Algunas recomendaciones son:

- Buscar un punto intermedio entre no documentar nada y documentar todo. Se debe realizar un ********tradeoff******** de que cosas viejas tomar, y cuales no
- Tener siempre en cuenta los objetivos de negocio
- Crear un mapa de dialogo con las principales interfaces del usuario
- Escribir historias de usuario o casos de uso principales de funcionalidades existentes y nuevos requisitos
- Derivar reglas de negocio
- Derivar modelo de dominio
- Desarrollar un diccionario de datos

# Requisitos en la Implementación de Paquetes

En este caso, nos compramos un producto y debemos implementarlo. Son proyectos complejos con muchas interfaces y requerimientos.

- Se pueden usar **************out of the box**************
- Se pueden configurar y usarlos
- Podemos integrarlo con otros sistemas (lo que requerirá algo de desarrollo)
- Podemos cometer el error de customizarlo, que llevara mucho trabajo. Generalmente es mejor adaptarse al paquete, en lugar de adaptar el paquete.

Suele haber una cantidad infernal de requisitos en estos paquetes. Llevan años en desarrollarse

!![[Apuntes/Análisis de la Información/attachments/Requisitos en Contexto 8.png]]

En general hay dos etapas:

- Evaluación y Selección del COTS: Proyecto en si mismo con su propia lista de requisitos
- Implementación del COTS

Los requisitos en cada etapa se manejan con distinto nivel de detalle, en la primera etapa son mas generales mientras que despues se detallan mas. Se deben analizar los requisitos, determinar la prioridad de los requisitos de los mismos. No siempre hay una solución perfecta.

# Requisitos en la Tercerización

- Muchas veces decidir tercerizar implica salir a buscar un proveedor.
- El cliente es el que especificara los requisitos. Se debe generar un RFP. Los requisitos deben poder ser modificables debido a cambios en el negocio.
- Debe haber condiciones de aceptación claras
- Equipo de trabajo esta en otro uso horario, o en otro idioma, esto trae dificultades.
- Falta conocimiento de negocio, puede dificultar el proceso.