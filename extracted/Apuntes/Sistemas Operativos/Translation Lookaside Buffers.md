# Translation Lookaside Buffers

Este método consiste en separar el espacio de direcciones en pequeños unidades (paginas) de tamaño fijo. Esta técnica requiere mucha información de ****mape****o. Por lo general esta información está almacenada en memoria física, se requiere acceder a cierta memoria extra, por cada dirección de memoria virtual. Por lo general, las páginas tienen un tamaño de ***4kb***. Aunque estos pueden variar según la implementación.

Este proceso de buscar en memoria la información para realizar la traducción es un proceso lento, por lo surge la pregunta: ¿cómo podemos acelerar el proceso de traducción de direcciones, evitando utilizar memoria extra?

Para esto, vamos a utilizar un elemento del hardware llamado ******TLB******, o ************************************************************************************translation-lookaside buffer************************************************************************************. Es una parte de la MMU, y es simplemente un *****caché***** de las traducciones *******virtual-física******* más populares. Un nombre más descriptivo podría ser *********************address-translation cache.*********************

<aside>
💡 El término ******RAM****** o ***************************************random-access memory*************************************** indica que se puede acceder a cualquier parte de la memoria tan rápido como cualquier otro. Sin embargo, debido a algunos rasgos de la computadora (como el ***TLB***), esto no es asi.

</aside>

# Funcionamiento del *TLB*

Ante cada referencia a memoria virtual, el ****hardware**** primero verifica si el TLB contiene la traducción deseada, en ese caso la traducción se realiza de forma rápida. En caso contrario, se debe consultar la **********page table**********, que contiene todas las traducciones.

Entonces, las direcciones virtuales están separadas en dos secciones: El número de página en el cual se encuentra la dirección de memoria (***vpn***, y un *offset*. Decimos que ocurre un ***************TLB hit*************** cuando el TLB contiene la dirección de memoria donde se encuentra la página deseada ). Entonces accede al valor y le suma el ******offset******.

Si la traducción deseada no se encuentra en el *TLB*, estamos ante un *****************TLB miss*.** La traducción entonces es agregada a la misma. Luego, se repite la búsqueda, pero de forma más eficiente ya que la traducción ahora se encuentra en la memoria caché.

Con el uso de paginación, podemos aumentar la velocidad de nuestro programa aprovechando la ******************localidad espacial******************, si usamos elementos cercanos en memoria, entonces la búsqueda puede ser rápida ya que guardamos las traducciones en el *TLB*. También existe el principio de la *********localidad temporal*********, se asume que si una dirección de memoria fue accedida, esta se volver a acceder pronto. En programación, los arreglos y los ciclos cumplen esta propiedad, favoreciendo los tiempos de ejecución.

Además de las traducciones, el buffer puede contener un *********valid bit*********, el cual indica si la información de esa traducción es válida. también *********protection bits*********, los cuales determinan que permisos tiene cierta pagina **(lectura, escritura, ejecución)**.

## *TLB miss*

Anteriormente, el **********hardware********** se encargaba completamente de lidiar con estos eventos, almacenando la información necesaria para todas las traducciones, se conocían como *********************hardware-managed TLBs*********************.

Las arquitecturas modernas, utilizan un *********************software-managed TLBs*********************. Cuando ocurre un *******TLB miss,******* el ********hardware******** lanza una excepción, el sistema operativo actualiza el caché y retorna del ****trap****. Este retorno es distinto al visto anteriormente, ante una system call, este debe volver a la instrucción siguiente al ****trap.**** En el caso de la TLB, el hardware debe seguir la ejecución en la instrucción que causó el ****trap****. Para esto, el ********hardware******** debe modificar el ***************program counter*************** antes de levantar la excepción.

Para que no ocurra una infinita cadena de **********TLB misses**********, entonces existen varias soluciones. Por ejemplo, se pueden almacenar los handlers en memoria física, donde no necesitan ser traducidos, o reservar algunas entradas del *****caché***** para ser siempre válidas.

# Context Switch

El buffer solo contiene traducciones válidas para el proceso que está actualmente corriendo en memoria. Estas traducciones no son válidas cuando se realiza un cambio de proceso. Una posible solución es la de indicar la invalidez de las traducciones con el *********valid bit*********. Esto puede ser ineficiente.

Para solucionarlo, algunos sistemas permiten compartir el buffer, añadiendo un campo ***********ASID*********** o ************************************************************************address space identifier************************************************.* Este campo permite diferenciar a que proceso le pertenece la traducción, para no acceder a memoria inválida.

# Política de Reemplazo

Como decidimos que entrada de la tabla sobreescribir cuando se añade una traducción a la misma. Hay distintos algoritmos para enfrentar el problema Uno muy común es ************LRU************ o ******************************************least-recently-used****************************.* Otra solución es utilizar una política aleatoria, cada solución es útil en distintos escenarios.

Cuando un programa accede en un corto periodo de tiempo a más páginas de las que puede almacenar el ***TLB***, entonces los accesos a memoria pueden volverse muy lentos. Nos referimos a este fenómeno como excederse del ************************************TLB coverage************************************. Una solución de este problema es incluir soporte para tablas de distintos tamaños.

Los accesos al TLB pueden rápidamente convertirse en un cuello de botella para el procesador, particularmente con lo llamado ********physically-indexed cache********. Para esta memoria, la traducción debe realizarse antes de que se acceda al caché, lo que puede ralentizar el proceso. Utilizar los **********************************virtually-indexed cache********************************** soluciona estos problemas de desempeño, pero introduce nuevos problemas en el diseño del hardware.