[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xkhqJnty)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21013784&assignment_repo_type=AssignmentRepo)
# Práctica: Búsqueda en Profundidad (DFS)

## Problema de las N Reinas

El **problema de las N reinas** consiste en colocar `N` reinas en un tablero de ajedrez de `N × N` de manera que **ninguna reina pueda atacar a otra**.  
Es decir, no puede haber dos reinas en la misma fila, columna o diagonal.

El uso de **DFS** para resolver el problema de las `N` reinas consiste en colocar una reina en una posición y luego explorar posiciones consecutivas que sean válidas según la definición del problema.

---

### Planteamiento de los ejercicios

En esta práctica se resolverán **tres ejercicios**, dos relacionados con el algoritmo DFS y uno relacionado con el algoritmo BFS:

---

#### Ejercicio 1

Definir una función en **Python** que reciba como entrada un entero `N` (`1 ≤ N ≤ 8`) correspondiente al tamaño del tablero.

La salida de la función es un **arreglo `P`** de tamaño `N` con enteros menores que `N` indicando una posible posición de las `N` reinas que soluciona el problema.

Si `i` es un valor menor a `N`, entonces el valor `P[i]` indica en qué **renglón de la i-ésima columna** del tablero colocar una reina para obtener una solución.

**Referencia:** además del pseudocódigo visto en clase, pueden revisar el siguiente enlace:  
[Visualización del problema de las N reinas (USFCA)](https://www.cs.usfca.edu/~galles/visualization/RecQueens.html)

---

##### Ejemplo

Supongamos que la función se llama `nreinas`, y la entrada de la función es `N = 4`.  
Una posible salida es:

`P = [1, 3, 0, 2]`

Esto corresponde al siguiente tablero:

|   |   | Q |   |
|---|---|---|---|
| Q |   |   |   |
|   |   |   | Q |
|   | Q |   |   |

Por lo tanto, el resultado de `nreinas(4)` es:

`[1, 3, 0, 2]`

---

#### Ejercicio 2

Definir una función en **Python** que reciba **dos entradas**:

1. Un entero `N` (`1 ≤ N ≤ 8`) correspondiente al tamaño del tablero.  
2. Un arreglo `A` de enteros tal que `0 ≤ len(A) ≤ N`.  
   (Es decir, puede ser un arreglo vacío, y puede tener a lo más `N` enteros que indican **posiciones no disponibles**.)

La salida de la función es un **arreglo `P`** de tamaño `N` que indica posiciones posibles para las `N` reinas que solucionan el problema.

---

##### Ejemplo

Supongamos que nuestra función se llama `nreinas2`, y que recibe como entradas:

`N = 4`  
`A = [1, 3, 0, 2]`

Una posible salida es:

`[2, 0, 3, 1]`

correspondiente al siguiente tablero:

|   | Q | X |   |
|---|---|---|---|
| X |   |   | Q |
| Q |   |   | X |
|   | X | Q |   |

> Las **X** indican posiciones no disponibles.

Por lo tanto, el resultado de `nreinas2(4, A)` es:

`[2, 0, 3, 1]`

---

### Punto Extra

Para cada uno de los dos problemas de las `N` reinas, si además del resultado que pide cada inciso, la función devuelve **todas las soluciones posibles**, entonces se obtiene **un punto extra** en la **tarea** correspondiente a estos temas.

---

## Problema del intervalo

Definir una función que reciba **dos datos de entrada**:

- Un arreglo `A` de enteros no negativos de tamaño `N > 0`.
- Un número racional no negativo `q`.

La salida producida por la función es **una lista con las dos posiciones** en el arreglo `A`, señalando el intervalo más pequeño que contiene al número `q`.

Para la definición de la función, dividir de manera **recursiva** el arreglo de entrada hasta obtener subarreglos con un solo dato (como en Merge Sort).

---

### Ejemplo

Supongamos que el número de entrada es:

`q = 8.13`  
`A = [4, 0, 7, 11, 9, 12, 56, 3]`

Para encontrar el intervalo más pequeño, la función divide el arreglo buscando:

- el entero que se aproxima **por abajo** de `q`, y  
- el que se aproxima **por arriba** de `q`.

El proceso interno puede visualizarse así:


```
[4, 0, 7, 11, 9, 12, 56, 3]
[4, 0, 7, 11]   [9, 12, 56, 3]
[4, 0] [7, 11]   [9, 12] [56, 3]
[4] [0] [7] [11]   [9] [12] [56] [3]
```



La función identifica que **7** y **9** son los enteros más cercanos a `q` por debajo y por arriba, respectivamente.

Por lo tanto, el resultado de la función con esas entradas es:

`[2, 4]`

donde los valores son las posiciones que ocupan el **7** y el **9** en el arreglo original.


---

# Parte II. Búsqueda en Anchura (BFS)

## Descripción del problema

Considera el siguiente **mapa de las ciudades de Rumania** (ver figura).  
Los valores que aparecen en las aristas corresponden al **tiempo promedio en minutos** que toma llegar desde un punto a otro con el que tenga conexión directa.  

Estos tiempos varían a lo largo del día, de acuerdo con el horario y las condiciones de tráfico.  
De manera específica, los tiempos de traslado se comportan así:

-  **De 00:00 a 5:59** → El tiempo de traslado es el que aparece en el mapa.  
-  **De 6:00 a 15:59** → El tiempo de traslado es **el doble** del que aparece en el mapa.  
  - Ejemplo: de **Bucharest a Giurgiu**, el tiempo de traslado es **180 minutos**.  
-  **De 16:00 a 23:59** → El tiempo de traslado entre cada dos puntos es **1.5 veces** el que aparece en el mapa.  
  - Ejemplo: de **Bucharest a Giurgiu**, el tiempo de traslado es **135 minutos**.

---

### Figura

**Figura 1.** Mapa de las ciudades de Rumania.  
*(Los valores en las aristas indican el tiempo promedio de traslado en minutos.)*

![Mapa de Rumania]((https://image1.slideserve.com/2592244/road-map-of-romania-l.jpg))

---

## Ejercicio

El objetivo de este ejercicio es **implementar un sistema** que pueda responder **cuál es el tiempo total de traslado** entre dos ciudades dadas, **considerando la hora de inicio del viaje**.

El cálculo debe **respetar los horarios** en los que cambian los tiempos estimados de traslado, de modo que si el viaje cruza un intervalo horario distinto, se debe ajustar el tiempo restante en consecuencia.

---

### Ejemplos

- **Ejemplo 1.**  
  Si el viaje es de **Giurgiu a Urziceni** y comienza a las **5:00 am**, entonces:
  - La primera parte del viaje (Giurgiu → Bucharest) dura **90 minutos**, porque inicia antes de las 6:00 am.  
  - Sin embargo, al llegar a Bucharest ya son **6:30 am**, y la segunda parte (Bucharest → Urziceni) ocurre después de las 6:00 am.  
    Por lo tanto, su duración se calcula con el **doble del tiempo** que aparece en el mapa, es decir **170 minutos**.

- **Ejemplo 2.**  
  Si el mismo viaje comienza a las **4:00 am**, ambos trayectos se calculan con el tiempo **original** del mapa, porque la llegada a Bucharest ocurre **antes de las 6:00 am**.

---

## Requisitos de implementación

- Utiliza el **algoritmo de Búsqueda en Anchura (BFS)** para recorrer el grafo de ciudades y determinar el camino más corto en número de aristas (no necesariamente en tiempo).
- Una vez encontrado el camino, **calcula el tiempo total del recorrido** ajustando los tiempos de cada tramo según el horario en que inicia.
- Se recomienda representar el grafo mediante un **diccionario de adyacencia** en Python.
- Considera representar el **horario de inicio** en formato de 24 horas (por ejemplo, `5.0` para 5:00 am o `13.5` para 13:30 pm).

---

### Sugerencias

- Puedes comenzar implementando una función `bfs_path(graph, start, goal)` que devuelva el camino más corto (lista de ciudades).
- Luego, define una función `travel_time(path, start_hour)` que calcule el tiempo total del recorrido considerando los horarios y ajustes de tráfico.
- Si lo deseas, imprime el recorrido y el tiempo acumulado entre cada ciudad intermedia.

---

