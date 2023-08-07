# Diseño de Datos

Los Archivos y bases las datos nos permiten que la información del sistema persista, cuando hablamos de modelado de datos, hablamos de tres niveles:

- ************************Conceptual:************************ Como un MDD, nos muestra las entidades y sus relaciones con otras entidades. No tiene nada que ver con la implementación, sino con el concepto
- ****************Lógico:**************** Diseño lógico de la base de datos/archivos. Debemos definir las tablas, las columnas, las claves primarias y foráneas.
- ************Físico************: Implementación de la base de datos: indices, espacios de almacenamiento, seguridad, etc.

# Bases de Datos

Una base de datos es una colección ordenada de datos administrada por un sistema de gestión (DBMS, Database Management System)

### Modelos de Base de Datos

Existen distintos modelos conocidos de base de datos:

- ********************Jerárquico:******************** Una fila de cabecera (master), y el detalle de los elementos de la base de datos (detail)
- ******De Red:****** Similar, pero sin necesidad de navegar la jerarquía, se puede navegar de un registro a otro
- ********************Relacional:******************** Tablas relacionadas entre si, por otras tablas:
    
    !![[Apuntes/Análisis de la Información/attachments/Diseño de Datos 3.png]]
    
    PRIMARY_KEY: id - FOREIGN KEY: user_id
    
    - Las claves primarias identifican las distintas filas (instancias) en una tabla
    - Las claves foráneas referencian a claves primarias de otras tablas y son empleadas para implementar las relaciones
- **Orientadas a** ************Objetos:************
- ******************Orientadas a Documento:****************** no estructuradas

# De Modelo de Dominio a Base de Datos

- Una tabla por cada objeto de dominio
- Una tabla para cada superclase y subclase o una tabla para cada una
    - Tendremos una única tabla, con un identificador de tipo para determinar a que subclase pertenece la entrada
    - Una tabla por cada variante, utilizando la misma clave foráneas en la subclase que refieren a la clave primaria de las primarias.
        
        A veces podemos suprimir superclase, si es una entidad abstracto y no hay elementos en común entre las subclases.
        
- Implementar las asociaciones:
    - *******One-Many:******* El lado de ****Many**** mantiene referencia al ***One*** a partir de una clave foránea
        
        !![[Apuntes/Análisis de la Información/attachments/Diseño de Datos 1.png]]
        
    - One-One****:**** Decidimos una tabla como mas relevante, e incluimos la *******foránea******* en la otra
    - **********Many-Many:********** Crear una tabla de correlación cuyas columnas serán las claves primarias de las tablas relacionadas. Los identificadores serán tanto claves primarias como foráneas
        
        !![[Apuntes/Análisis de la Información/attachments/Diseño de Datos 2.png]]
        
    - ***********Recursivas: Para cualquier tipo de cardinalidad, t***********endremos una tabla de correlación que una dos claves de la misma tabla.
    - Asociativas: Necesitaremos una tabla asociación con atributos propios de la asociación
    
    # Normalización
    
    Buscamos evitar la redundancia de datos, la normalización es una herramienta para eliminar la redundancia. Debemos verificar tres reglas:
    
    1. No hay atributos repetitivos
    2. En registros con claves compuestas, todos los atributos no clave son funcionalmente dependientes de toda la clave
    3. Todos los atributos son funcionalmente dependientes de la clave, no hay dependencias transitivas