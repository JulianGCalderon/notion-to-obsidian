# Notion a Obsidian

Después de usar Notion para tomar notas de la facultad por dos años, me di cuenta de que el objetivo principal de Notion era el de gestión de proyectos y organización, y que le faltaban buenas características para la simple toma de notas, además de que el uso de un lenguaje de marcado propietario dificulta la migración de las notas a otro software. Migré a Obsidian.

## ¿Cómo exporta Notion?

Notion exporta a Markdown de forma nativa, pero la carpeta que genera tiene un par de errores:

- Todos los archivos.md y las carpetas finalizan su nombre con un UUID, lo cual es molesto.
- Notion utiliza Katex, mientras que Obsidian utiliza Mathjax
- Los pies de foto en Markdown no están permitidos, por lo que Notion descarta esa información al exportar (lo deja como un texto normal)
- Los callouts de Notion se logran al exportar a través de HTML puro, lo cual no queda bien fuera de Notion.
- Los textos en negrita e itálica se exportan mal, dejando muchos asteriscos a cada lado del texto.
- El título del archivo se agrega como H1 al comienzo del archivo

## Características del Script

El script soluciona alguno de los errores mencionados:

- Elimina el UUID de los archivos y carpetas
- Convierte las ecuaciones de Katex a Mathjax a través de Regex
- Convierte todos los links a formato OFM (Obsidian Flavoured Markdown)
- Convierte los callouts de Notion a un formato compatible con Obsidian
- No arregla los asteriscos de negrita e itálica, pero reduce la cantidad de asteriscos de 4+ a 3. Esto sigue siendo un problema, ya que Obsidian los reconocerá a todos como negrita. Los tuve que arreglar a mano, pero no es tan difícil.
- Elimina el título del archivo al comienzo del archivo

## Sugerencias

Luego de ejecutar el Script, recomiendo algunas extensiones:

- **Linter**: Para arreglar errores pequeños que puedan quedar luego de la conversión. En particular, tiene una opción para trasladar todos los títulos H1 a títulos H2, y así. Esto permite que el único título H1 de cada archivo sea el nombre del mismo.
- **LangaugeToolIntegration**: Ofrece una mejor corrección ortográfica en español (mucho mejor que la opción nativa, y la ofrecida por Notion)
- **Mousewheel Image Zoom**: Permite agrandar y achicar las imágenes de forma más cómoda.
- **Obsidian Git**: Permite hacer una copia de seguridad de tus notas en la nube, a través de un repositorio de Git.

## Hosting

Obsidian ofrece un servicio de hosting de pago, si se quiere una opción gratuita, sugiero investigar _Quartz_, una plantilla para hostear notas en Markdown (con soporte para Obsidian) como una página web estática.
