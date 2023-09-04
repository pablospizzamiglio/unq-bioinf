# Bioinformática - TP 1

## Desafío 1

Ejemplo de macromoléculas que almacenen información sobre la "identidad" de un organismo dado:

Ácidos nucleicos

Son las moléculas que contienen la información genética que dirige y controla la síntesis de proteínas de un organismo. También proporcionan la información que determina la especificidad y características biológicas de las proteínas. Entre ellos se encuentran:

- ADN
- ARN

## Desafío 2

Como existen 22 aminoácidos, y estos se representan con una letra del alfabeto, la información contenida en la estructura primaria de las proteínas podría expresarse como una secuencia de caracteres. En Python se vería similar a:

```python
s = "CGTAACAAGGTTTCCGTAGGTGAACC..."
```

## Desafío 3

Ya que la estructura terciaria de una proteína plegamiento tridimensional de las proteínas debido a las interacciones de sus cadenas laterales, se puede representar de la siguiente como un diccionario de tuplas que contienen coordenadas en el espacio de tres dimensiones, la clave de este diccionario debería seguir el orden de la secuencia de aminoácidos. En Python, se vería de la siguiente manera:

```python
t = {
  "C": (x1, y1, z1),
  "G": (x2, y2, z2),
  "T": (x3, y3, z3),
  # ...
  "G": (xn, yn, zn),
}
```

## Desafío 4

Aportes de Rosalind Franklin:

- Es conocida por su trabajo pionero en la obtención de imágenes de difracción de rayos X de fibras de ADN. A partir de estas imágenes, pudo deducir información crucial sobre la estructura del ADN, como su forma helicoidal y las dimensiones de la hélice.

- Sugirió la existencia de diferentes formas de ADN, siendo la forma B-DNA la más común en las condiciones biológicas. Esta forma helicoidal y más amplia del ADN es esencial para la replicación y transcripción del material genético.

- Investigó la estructura de las fibras proteicas, como el virus del mosaico del tabaco y las proteínas del colágeno. Sus estudios en este campo proporcionaron información valiosa sobre la organización y estructura de las proteínas.

- Realizó investigaciones pioneras sobre la estructura del virus del mosaico del tabaco, demostrando que estaba compuesto principalmente de proteínas. Este trabajo contribuyó al entendimiento de los virus como entidades biológicas.

- Aunque James Watson y Francis Crick son generalmente acreditados con el descubrimiento de la estructura del ADN en 1953, la investigación de Franklin fue esencial en la obtención de datos cruciales que respaldaron la propuesta de la doble hélice de ADN. Las imágenes de difracción de rayos X de Franklin sirvieron como una fuente importante de inspiración e información para Watson y Crick en su modelo.

## Desafío 5

Ver archivo `predictor.py`.

## Desafío 6
