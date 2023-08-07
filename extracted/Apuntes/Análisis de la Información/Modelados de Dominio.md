# Modelados de Dominio

Un modelo de dominio es una representación visual del vocabulario del dominio.  Los construimos para entender y analizar mejor el contexto en el que operará el sistema a desarrollar.

Los objetos de dominio tienen atributos, que caracterizan a los objetos, y están relacionados entre si por cierta asociación.

# ¿Categorías?

En general, los objetos de dominio pertenece a las siguientes familias:

- Cosas manipuladas en una organización (contratos, facturas, pedidos)
- Objetos y conceptos del mundo real que el sistema debe conocer om monitorear (avión, misil, trayectoria)
- Eventos pasados a futuro (arribo, partida, pago)
- Personas, roles, organizaciones (cliente, socio, alumno)

# Objetos de Diseño

Estos no son los objetos de diseño, no contienen detalles de la implementación. Los objetos de diseño están inspirados en conceptos del dominio del problema. La orientación a objetos busca minimizar la brecha entre el vocabulario del problema y la solución. No todo objeto de diseño existe en el dominio del problema.

# ¿Cómo se Construye?

En general, tiene los siguientes pasos:

1. Identificar clases conceptuales
2. Dibujarlas en un diagrama de clases
3. Agregar asociaciones y atributos
4. Agregar generalizaciones, especializaciones, composiciones, agregaciones

Es un proceso iterativo e incremental. Lo importante no es el resultado sino identificar los grandes objetos que forman parte del dominio.

Existen tres estrategias básicas para encontrar las clases conceptuales:

- Aplicar el análisis lingüístico: Buscamos en nuestras minutas de Reunión, especificaciones y casos de uso, sustantivos que puedan ser candidatos a clases. El lenguaje natural es ambiguo. No podemos aplicar este enfoque de forma mecánica. Es preferible combinar esta técnica con la lista de categorías.
- Utilizar una lista de categorías: A partir de una lista predefinida de categorías de objetos, podemos guiarnos para encontrar los objetos de nuestras clases del modelo dominio:
    - Transacciones
    - Items de una transacciones
    - Producto o servicio relacionado con la transacción
    - Donde se registra la transacción
    - Roles u organizaciones relacionadas
    - Lugar de la transacción
    - Eventos
    - Objetos físicos
- Reutilizar un modelo ya existente

# Atributos

Un atributo es un dato lógico acerca de un objeto. Es información que debe ser recordada por el sistema

Siempre son tipos de datos primitivos: numérico, lógico, fecha, tiempo, texto. No se deben incluir atributos que referencian a otras clases

Algunos atributos son identificadores naturales (permiten individualizar una instancia particular de una clase, este suele indicarse con el estereotipo *{id}*.

En algunos casos puede ser importante mostrar atributos derivados a partir de otros atributos (cuando sea relevante para entender el dominio)

# Asociaciones

Una **asociación** es una relación entre instancias de una clase conceptual que debe ser recordada por el sistema. Casa asociación tiene nombre (frase con verbo) y multiplicidad. 

La **multiplicidad** indica una regla de negocio (cardinalidad). Pueden existir múltiples asociaciones entre dos clases. 

Típicamente las asociaciones son binarias, pero puede tener **asociaciones binarias** (en las que participan dos objetos). También podemos encontrar **asociaciones unarias** (entre instancias de una misma clase conceptual)

 En menor proporción, es posible encontrar **asociaciones ternarias** (entre tres tipos de objetos). Las asociaciones entre más de tres objetos no son habituales.

Las **clases asociativa**s se comportan simultáneamente como clase y como asociaciones. Se descubren ante la necesidad de asociar un atributo a una asociación.

Las asociaciones de **composición y agregación** permiten modelar relaciones del tipo todo y parte. Cuando los elementos de la conexión no dependen del ciclo de vida del contenedor, estamos ante una agregación. Cuando o hacen, estamos ante una composición.

Las **asociaciones calificadas** permiten distinguir un grupo de instancias en uno de los extremos mediante un calificador. Por ejemplo: Todas las materias pertenecientes al mismo departamento se identifican con el código del departamento. 

Muchas veces, queremos establecer generalizaciones y especializaciones. Definimos aspectos **comunes** (superclase) ****y aspectos ************particulares************ (subclase). Es necesario cuando la subclase tiene atributos o asociaciones adicionales a los de la superclase

Un ******rol****** en uno de los extremos de una asociación describe el papel que juega el objeto en la relación. No son obligatorios, pero pueden ayudar a entender mejor larelación entre los objetos.

Para encontrar asociaciones podemos utilizar una lista de categorías predefinidas.

# Patrones

Cuando tenemos objetos con atributos comunes y otros que los diferencian, podemos utilizar la generalización y la especificación para mejorar el modelado.

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 8.png]]

Para modelar estructuras jerárquicas, podemos utilizar asociaciones genéricas.

Existe una unidad organizacional que puede tener múltiples unidades organizacionales que le corresponden. Y cada una pertenece a un tipo particular.

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 1.png]]

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 2.png]]

A veces, es necesario separar la descripción o especificación del producto de una instancia de dicho producto.

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 3.png]]

Muchas veces es necesario registrar movimientos y saldos de bienes y valores. Para transferir plata entre cuentas, utilizamos transacciones. Las transacciones tienen dos movimientos asociados (uno para debitar, y otro para acreditan. A veces, las cuentas agrupan uentas de menor nivel

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 4.png]]

Muchas veces, necesitamos registrar mediciones. Separamos entonces en el objeto medido, la medición, y el tipo de medición

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 5.png]]

# Factura

Una factura es un documento que refleja la información de una operación de venta. En general, cada país tiene regulaciones que indican como deben generarse y resguardarse. En muchos países, existe la factura electrónica. Los sistemas administrativos necesitan mantener esta información.

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 6.png]]

Además de facturas, existen notas de credito y debito. Las notas de crédito disponen de saldo a favor al cliente, mientras que las notas de débito reflejan un saldo a favor del vendedor. 

!![[Apuntes/Análisis de la Información/attachments/Modelados de Dominio 7.png]]

# Modelo de Datos

Propone modelar entidades y relaciones. DEs un modelo conceptual que sirev para luego derivar los modelos logicos y fisicos de  la base de los datos. Es un antecesor del modelo de dominio. Tiene los siguientes elmentos:

- Entidades: Abstracciones que representan personas, osas, lugares. Atributos identificadores y descriptivos de las entidades. Algunos tipos de objetos son tambie nrealciones (asociativos) y otro son debiles (su indentificaión depende de otra identidad)
- Relaciones: Es una abstraccion que representa la asosiacion

Algunas diferencias importantes son:

- Si un objeto no es instanciable, no es un objeto.
- Cada objeto tiene un identificador.

Existen distintas comunidades, con distintas perspectivas del modelado de datos y objetos:

- **Diseño de base de datos:** Trabajan en el espacio de la solución y estan preocupados por el modelo logico de la base de datos
- **Modelado conceptual**: Trabajan en el espacio del problema, los datos son activos en la organización. Están preocupados por la arquitectura de los datos, independientementede la tecnología.
- ******************************************Modelado de objetos:****************************************** Mas cerca del espacio de la solución. Todo es un objeto

UML se puede utilizar para modelar en las tres situaciones, con algunas salvedades en cuanto a la notación. En determinados contextos el modelado entre distintas perspectivas es importante. El modelado de dominio es equivalente al modelo conceptual de datos.