# Horus
  Motivados por la falta de herramientas que permitan la accesibilidad a personas con capacidades motoras reducidas, decidimos desarrollar una herramienta multipropósito que permita diversas aplicaciones, desde una silla de ruedas hasta controlar un mouse, todo esto mediante la detección de la dirección en el que se mira. Para esto diseñamos y entrenamos una red neuronal convolucional que clasifica las direcciones: derecha, izquierda, centro y los ojos cerrados. A partir de esto se le pueden dar infinidad de usos a esta herramienta, la cual alcanzó resultados muy satisfactorios, con una tasa de acierto de más del 98%. Para fines demostrativos haremos una analogía entre controlar una silla de ruedas y controlar el robot butiá. En el siguiente documento incluimos una breve introducción a los conceptos de redes neuronales, convolucionales y distintas métricas, también incluiremos los resultados obtenidos, así como una guía para su replicación e implementación.



# Arquitectura de la red
## Sobre el diseño de nuestra red
Nuetra Red presenta las siguientes capas

-> Convolución de 32 filtros de un tamaño de 16x16.

-> Max Pooling de tamaño 4x4.

-> Convolución de 16 filtros de un tamaño de 8x8.

-> Max Pooling de tamaño 4x4.

-> Aplanado de imágen a un tamaño de 400.

-> Dropout de 256 neuronas.

-> Capa densa de 256 neuronas.

-> Capa final o capa de salida con las 4 categorías que queremos detectar.

A continuacion un diagrama que representa el modelo.

![image](https://user-images.githubusercontent.com/59852188/121453548-ba5ed380-c977-11eb-8edb-384907c0af3c.png)

# Sobre los resultados
Obtuvimos una taza de acierto superior al 98 %. A continuacion se presenta la matriz de confucion para el modelo con un total de 20 % del dataset el cual es nuestro set de validacion.

# Matriz de confusion
![Confucion matrix](https://user-images.githubusercontent.com/59852188/121453345-681db280-c977-11eb-976e-668efb692438.png)

# Aspectos interesantes
Como el modelo utilizado es una red neuronal convolusional podemos obtener los feature maps para poder visualizar que es lo que "ve" nuestro modelo. Supongamos la siguiente imagen de entrada (Extraida de nuestro set de datos).
![image](https://user-images.githubusercontent.com/59852188/121791666-ca1e2800-cbc2-11eb-92cb-a3dcba162f4d.png)
A continuacion veamos que de la primera convolusion podemos extraer mapas de caracteristicas que se asemejan mucho a un ojo.
![image](https://user-images.githubusercontent.com/59852188/121791685-f043c800-cbc2-11eb-9bcd-1e346821319b.png)

# Funciones del modulo interfazButiaTelnet
connect(HOST,PORT) : Conecta al servidor del Butiá en el host HOST y puerto PORT. (HOST es la ip)

mover(TN,DIRECCION) : Envía la señal de mover al robot Butiá según la dirección pasada por parámetro, siempre se mueve a una velocidad de 100.

Por mas informacion leer la documentacion que se encuentra en este mismo repositorio (informe.pdf)

# Autores
Federico Gil & Facundo Felitas
