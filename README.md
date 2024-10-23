# Creación de máquina virtual
- - -
## Introducción
Con el fin de crear nuestra propia máquina virtual, hemos usado Python y algunas librerías. Además, nos basaremos en la estructura de la pila para poder realizar el programa. Nuestro programa estará basado en la *Fashion Show de Victoria’s Secret 2024*. Durante la ejecución, se vestirá a una modelo con diferentes accesorios, como el peinado, las alas y los zapatos. Cabe añadir que los accesorios que se pueden elegir para vestir a las modelos, estarán almacenados en una memoria. Asimismo, se tendrán una serie de modelos preestablecidas que vestirán diferentes accesorios. En el caso de que la modelo que se cree ya se encuentre almacenada en memoria, se mostrará un video suyo durante el desfile. 

## Manual de ejecución
Este programa se ha ejecutado mediante la aplicación de Visual Studio Code.
[Descargar Visual Studio Code](https://code.visualstudio.com/download) 
En esta aplicación se ha instalado Python, y en concreto se ha ejecutado y comprobado su correcto funcionamiento en la ***versión Python 3.13.0***. 
[Tutorial Python](https://code.visualstudio.com/docs/python/python-tutorial)
Asimismo, se importarán las librerías **os** y **platform**, como se muestra al inicio del código del archivo **VM.py** para poder visualizar el video en un dispositivo Mac.

	import os
	import platform

Es importante mencionar que se tendrán dos archivos diferentes. En el primero, **VM.py**,  se tendrá el código de la pila,  el de la máquina virtual y el `__main__`. En el segundo archivo, **desfile.fais**, se tendrán las instrucciones que se van a ejecutar. Este último tendrá una extensión creada por nosotras. De la misma forma, se deberán haber descargado previamente los videos de las modelos durante el desfile. La ruta donde se tengan guardados estos videos deberá ser modificada dentro del `__init__` de la clase `StackVM()`. 

Para poder ejecutar el programa se debe ir a la terminal, y dentro de esta a la carpeta donde se tengan almacenados los archivos correspondientes. A continuación, se ejecutará el comando <code>python VM.py  desfile.fais</code> . Por último, se mostrarán los resultados impresos en la terminal. 

Para poder hacer que salten los videos deben de descargarse los videos y modificar la ruta de acceso en la línea 93.

## 1. Estructurar el proyecto
El primer paso, para crear este programa ha sido crear un pequeño esquema, para estructurar el programa. Se tendrán diferentes pilas y una memoria inmodificable a la que se accede para ver los diferentes modelos almacenados. Además, se tendrá una lista de elementos permitidos para cada categoría, es decir, para los nombres de las modelos, los peinados, las alas y los zapatos. 

<img width="350" alt="Captura de pantalla 2024-10-20 a las 14 22 49" src="https://github.com/user-attachments/assets/ebcaed79-b196-4cf2-9001-54e3482d84ba">

## 2. Código
El código contiene pilas, funciones y una Máquina Virtual, donde la Clase Pila y la clase Máquina Virtual (VM), se explicarán detalladamente luego. El código empieza inicializando la clase Pila, luego tenemos la función de `obtener_tipo()`, en la cual se fija el tipo de elemento, ya sea modelo, peinado, alas o zapatos, para poder clasificarlos y luego poder usarlo para verificar que tenemos solo un elemento de ese tipo. Después, se inicia la clase StackVM, que será explicada más adelante. Por último, tenemos el programa `__main__`, que nos dejara usar el comando <code>python VM.py nombreDelArchivo.Extension</code> que en este caso la extensión es **.fais**.

###Clase Pila 
Para empezar, las pilas son estructuras de datos que siguen el principio LIFO, es decir, el último elemento que entra es el primero en salir. El cual tiene unas operaciones básicas como `pop()`, `peek()`, `push()`y `is_empty()`, cada una tiene su función. Por ejemplo, con el `pop()` se elimina el último elemento insertado en la pila; con `push()` se introduce a la última posición un elemento; con el `peek()` sacas el último elemento insertado; y el `is_empty()` verifica si la pila está vacía.
En esta clase, aparte de los comandos básicos, hemos creado otras dos operaciones que son: `size()` y `contains()`. `size()` devuelve la cantidad de elementos que están en la pila, y `contains()` devuelve si el elemento que se introduce lo tiene puesto la modelo o no.

###Clase MV 
Se creará una Máquina Virtual basada en pilas, donde podremos vestir a una ‘modelo’ que guardará los accesorios que se ponga en una pila. Dentro de la Máquina Virtual tenemos una pila que será **vestir**, en las cual se guardará información diferente dependiendo de cada uno de los elementos insertados. Los elementos se encuentran en listas, estas son: **modelos, peinados, alas y zapatos**. Tendremos guardado unos outfits en un registro de memoria y unos links de videos, los cuales estarán relacionados más adelante. 

Se tienen cuatro funciones: `comparar_outfit()`, `completo()`, `interpretar_comando()` y `execute()`. 
En la función `completo()`, se verifica si en la pila `vestir` tenemos el outfit completo o no. Si no se tiene un elemento, te dirá cual falta y pondrá que el outfit es original. También se fijará que solo haya un elemento de cada tipo.
En `comparar_outfit()`, como indica su nombre, hacemos que se comparen los outfits que tenemos en el registro de memoria con el outfit creado por el usuario, si el outfit creado coincide con uno de la memoria, lo redirigirá a un video de ese outfit; y si no, te dirá que has creado un outfit original. 
En `interpretar_comando()`, como también indica su nombre, es para poder interpretar los diferentes comandos que tenemos, que son: `PUSH_MODELO`, el cual introduce a la pila `vestir` el nombre de una modelo; `PUSH_PEINADO`, el cual introduce en la pila `vestir` un tipo de peinado; `PUSH_ALAS`, el cual introduce en la pila `vestir` el color de las alas; `PUSH_ZAPATOS`, el cual introduce en la pila `vestir` el tipo de zapatos; `EMPTY`, el cual verifica si la pila `vestir` está vacía; `POP`, el cual elimina el último elemento insertado en la pila `vestir`; `DESFILAR`, el cual hace uso de la función `completo()` para verificar si el outfit tiene elementos de todos los tipos sin que se dupliquen, y si falta alguno indicará cual es; `CAMBIAR_ALAS`, el cual saca las alas actuales de la pila `vestir` y las cambia por otras con otro color; `PEEK`, el cual muestra por pantalla el último elemento de la pila `vestir`; `COMPARE`, el cual hace uso de la función `comparar_outfit()` para comparar los outfits del registro de memoria con el creado y así poder ver si se muestra un video o no; `SIZE`, el cual dice cuantos elementos hay en la pila `vestir`; y `CONTAINS`, el cual muestra si el elemento puesto como argumento lo tiene puesto la modelo o no.
La función `execute()` es para ejecutar el archivo **.fais** con los comandos que se introducen.

## 3. Archivo desfile.fais
Este archivo tiene una extensión creada por nosotras, que es **.fais** y la cual corresponde a las iniciales de nuestros nombres. 
Al inicio del programa, se mostrarán las diferentes opciones de modelos, peinados, alas y zapatos que se pueden insertar en la pila. Además, se ejecutarán las diferentes instrucciones definidas en el archivo **VM.py** que serán `EMPTY`, `PUSH_MODELO`, `PUSH_PEINADO`, `PUSH_ALAS`, `PUSH_ZAPATOS`, `CONTAINS`, `DESFILAR`, `POP`, `PEEK`, `SIZE`, `COMPARE`. Mediante el uso de estas instrucciones, se insertarán, cambiarán y borrarán elementos de las pilas. Asimismo, se observarán todos los cambios que se realicen en la pila `vestir`.  

## 4. Conclusión
Gracias al uso de la herramienta Visual Studio Code y del lenguaje Python ha sido posible la creación de una máquina virtual para crear y vestir a diferentes modelos del Fashion Show, mediante el uso de la estructura de datos “pila” y a la memoria predefinida de modelos. 

## Bibliografía
- [Visual Studio Code](https://code.visualstudio.com/download) 
- [Tutorial Python](https://code.visualstudio.com/docs/python/python-tutorial)

## Creadoras
- 👤 **Amanda Aroutin** - [GitHub](https://github.com/amandaaroutin) 
- 👤 **Flor Portada** - [GitHub](https://github.com/florportada) 
- 👤 **Iria Prados** - [GitHub](https://github.com/iriaprados) 
- 👤 **Sonia Specht** - [GitHub](https://github.com/soniaspecht) 
