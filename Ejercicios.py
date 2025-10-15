#Ejercicio 1 con punto extra:)
def leer_n():
    # Lee N en [1, 8]
    while True:
        txt = input("Ingresa N (1 a 8): ")
        txt = txt.strip()
        if txt.isdigit():
            n = int(txt)
            if 1 <= n <= 8:
                return n
        print("Dato inválido. Intenta de nuevo.")

def hay_conflicto(tablero, col):
    """
    Verifica ataques por fila o diagonal contra reinas en columnas anteriores.
    """
    fila = tablero[col]
    c = 0
    while c < col:
        fila_ant = tablero[c]
        if fila == fila_ant:
            return True
        if abs(fila - fila_ant) == abs(col - c):
            return True
        c = c + 1
    return False

def dfs_colocar(tablero, col, n):
    # Coloca recursivamente una reina por columna (una sola solución)
    if col == n:
        return True
    fila = 0
    while fila < n:
        tablero[col] = fila
        if not hay_conflicto(tablero, col):
            if dfs_colocar(tablero, col + 1, n):
                return True
        fila = fila + 1
    tablero[col] = -1
    return False

def nreinas(n):
    # Devuelve una sola solución o [] si no existe
    if not isinstance(n, int):
        return []
    if n < 1 or n > 8:
        return []
    tablero = [-1] * n
    exito = dfs_colocar(tablero, 0, n)
    if exito:
        return tablero
    return []

def todas_nreinas(n):
    # Devuelve una lista con todas las soluciones
    if not isinstance(n, int):
        return []
    if n < 1 or n > 8:
        return []
    P = [-1] * n
    soluciones = []

    def sin_conflicto(col):
        fila = P[col]
        c = 0
        while c < col:
            if P[c] == fila:
                return False
            if abs(P[c] - fila) == abs(c - col):
                return False
            c = c + 1
        return True

    def dfs(col):
        if col == n:
            soluciones.append(P[:])
            return
        fila = 0
        while fila < n:
            P[col] = fila
            if sin_conflicto(col):
                dfs(col + 1)
            fila = fila + 1
        P[col] = -1

    dfs(0)
    return soluciones

def imprimir(P):
    if len(P) == 0:
        print("Sin solución.")
        return
    n = len(P)
    r = 0
    while r < n:
        c = 0
        linea = ""
        while c < n:
            if P[c] == r:
                ch = "Q"
            else:
                ch = "."
            if c > 0:
                linea = linea + " "
            linea = linea + ch
            c = c + 1
        print(linea)
        r = r + 1

def imprimir_todas(lista):
    i = 0
    while i < len(lista):
        print("Solución", i + 1, ":", lista[i])
        imprimir(lista[i])
        i = i + 1

# SALIDA
N = leer_n()
sol = nreinas(N)

if len(sol) == 0:
    print("No existe solución para N =", N)
else:
    print("Solución P:", sol)
    imprimir(sol)

todas = todas_nreinas(N)
print("Total de soluciones:", len(todas))

if len(todas) > 0:
    resp = input("¿Mostrar todas las soluciones? (s/n): ")
    resp = resp.strip()
    resp = resp.lower()
    if resp == "s":
        imprimir_todas(todas)

#EJERCICO 2 CON PUNTO EXTRA ------------------------------------------------------------------------------------------------------------------------------------

def nReinasUna(n, bloqueos):
    # DFS + backtracking respetando bloqueos: bloqueos[col] = fila prohibida
    tablero = [-1] * n

    def estaBloqueada(columna, fila):
        return columna < len(bloqueos) and fila == bloqueos[columna]

    def sinConflicto(columna):
        fila = tablero[columna]
        prev = 0
        while prev < columna:
            if fila == tablero[prev]:
                return False
            if abs(fila - tablero[prev]) == abs(columna - prev):
                return False
            prev = prev + 1
        return True

    def buscar(columna=0):
        if columna == n:
            return True
        fila = 0
        while fila < n:
            if not estaBloqueada(columna, fila):
                tablero[columna] = fila
                if sinConflicto(columna):
                    if buscar(columna + 1):
                        return True
            fila = fila + 1
        tablero[columna] = -1
        return False

    ok = buscar(0)
    if ok:
        return tablero[:]
    return []

def todasNReinas(n, bloqueos):
    # Devuelve lista de TODAS las soluciones respetando bloqueos
    solucion = [-1] * n
    listaSoluciones = []

    def estaBloqueada(columna, fila):
        return columna < len(bloqueos) and fila == bloqueos[columna]

    def sinConflicto(columna):
        fila = solucion[columna]
        prev = 0
        while prev < columna:
            if fila == solucion[prev]:
                return False
            if abs(fila - solucion[prev]) == abs(columna - prev):
                return False
            prev = prev + 1
        return True

    def buscar(columna=0):
        if columna == n:
            listaSoluciones.append(solucion[:])
            return
        fila = 0
        while fila < n:
            if not estaBloqueada(columna, fila):
                solucion[columna] = fila
                if sinConflicto(columna):
                    buscar(columna + 1)
            fila = fila + 1
        solucion[columna] = -1

    buscar(0)
    return listaSoluciones

# Impresion de las cuadriculas 
def imprimirTablero(solucion, n, bloqueos):
    """
    Dibuja tablero n×n:
    - 'Q' reina (según solucion)
    - 'X' casilla bloqueada (según bloqueos)
    - '.' vacío
    """
    def valorCelda(renglon, columna):
        if columna < len(bloqueos) and bloqueos[columna] == renglon:
            return "X"
        if solucion and solucion[columna] == renglon:
            return "Q"
        return "."

    separador = " ".join([""] * n)
    r = 0
    while r < n:
        print(separador)
        fila = []
        c = 0
        while c < n:
            fila.append(" " + valorCelda(r, c) + " ")
            c = c + 1
        print(" " + " ".join(fila) + " ")
        r = r + 1
    print(separador)

def imprimirTodas(listaSoluciones, n, bloqueos):
    i = 0
    while i < len(listaSoluciones):
        print("Solución", i + 1, ":", listaSoluciones[i])
        imprimirTablero(listaSoluciones[i], n, bloqueos)
        i = i + 1

# Entrada de datos 
def leerN():
    while True:
        texto = input("Ingresa N (1 a 8): ")
        texto = texto.strip()
        if texto.isdigit():
            n = int(texto)
            if 1 <= n <= 8:
                return n
        print("Dato inválido, intenta de nuevo.")

def leerBloqueos(n):
    texto = input("Ingresa filas bloqueadas por columna (ej: 1,3,0,2) o vacío: ")
    texto = texto.strip()
    if texto == "":
        return []
    partes = [p.strip() for p in texto.split(",")]
    bloqueos = []
    i = 0
    while i < len(partes):
        p = partes[i]
        if not p.isdigit():
            print("Valor no entero en bloqueos. Usando lista vacía [].")
            return []
        v = int(p)
        if v < 0 or v >= n:
            print("Valor fuera de [0, n-1]. Usando lista vacía [].")
            return []
        bloqueos.append(v)
        i = i + 1
    if len(bloqueos) > n:
        bloqueos = bloqueos[:n]
    return bloqueos
#Menu 
def main():
    n = leerN()
    bloqueos = leerBloqueos(n)

    # Una solución
    solucion = nReinasUna(n, bloqueos)
    if len(solucion) == 0:
        print("No existe solución con esas restricciones.")
    else:
        print("Solución P:", solucion)
        imprimirTablero(solucion, n, bloqueos)

    # Todas las soluciones
    listaSoluciones = todasNReinas(n, bloqueos)
    print("Total de soluciones:", len(listaSoluciones))
    if len(listaSoluciones) > 0:
        resp = input("¿Mostrar todas las soluciones? (s/n): ")
        resp = resp.strip()
        resp = resp.lower()
        if resp == "s":
            imprimirTodas(listaSoluciones, n, bloqueos)

main()

#-------------------------------------------------- EJERCICIO 3: INTERVALO --------------------------------------------------

from typing import List, Optional, Tuple

#Busca en el Arreglo los valores mas cercanos (por arriba y por abajo) a q usando dfsBsucar y devuelve los indices de estos en el arreglo
def intervaloIndices(arreglo: List[int], numeroQ: float) -> List[int]:
    # Validaciones
    n = len(arreglo)
    if n <= 0:
        raise ValueError("El arreglo debe tener N > 0")
    if numeroQ < 0:
        raise ValueError("El numero q no puede ser negativo")

    #Guardamos pares (valor, índice) para no perder posiciones
    paresValorIndice = []
    i = 0
    while i < n:
        par = (arreglo[i], i)
        paresValorIndice.append(par)
        i = i + 1

    #Regresa el mejor valor menor/igual a q y el valor igual/mayor a q
    def dfsBuscar(ini: int, fin: int) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
        if fin - ini == 1:
            valor = paresValorIndice[ini][0]
            indice = paresValorIndice[ini][1]
            candidatoInferior = None
            candidatoSuperior = None
            if valor <= numeroQ:
                candidatoInferior = (valor, indice)
            if valor >= numeroQ:
                candidatoSuperior = (valor, indice)
            return candidatoInferior, candidatoSuperior

        medio = ini + (fin - ini) // 2
        inferiorIzq, superiorIzq = dfsBuscar(ini, medio)
        inferiorDer, superiorDer = dfsBuscar(medio, fin)

        mejorInferior = inferiorIzq
        if inferiorDer is not None:
            if mejorInferior is None:
                mejorInferior = inferiorDer
            else:
                if inferiorDer[0] > mejorInferior[0]:
                    mejorInferior = inferiorDer

        mejorSuperior = superiorIzq
        if superiorDer is not None:
            if mejorSuperior is None:
                mejorSuperior = superiorDer
            else:
                if superiorDer[0] < mejorSuperior[0]:
                    mejorSuperior = superiorDer

        return mejorInferior, mejorSuperior

    mejorInferior, mejorSuperior = dfsBuscar(0, n)

    #Si q coincide exactamente con un valor, usamos el mismo índice
    if mejorInferior is not None and mejorSuperior is not None and mejorInferior[0] == mejorSuperior[0]:
        indice = mejorInferior[1]
        return [indice, indice]

    #Si falta un lado, repetimos el disponible
    if mejorInferior is None and mejorSuperior is not None:
        return [mejorSuperior[1], mejorSuperior[1]]
    if mejorSuperior is None and mejorInferior is not None:
        return [mejorInferior[1], mejorInferior[1]]

    #Ambos lados existen
    if mejorInferior is not None and mejorSuperior is not None:
        return [mejorInferior[1], mejorSuperior[1]]

    raise RuntimeError("No se pudo determinar el intervalo.")

#Ejemplo
if __name__ == "__main__":
    numeroQ = 8.13
    arreglo = [4, 0, 7, 11, 9, 12, 56, 3]
    posiciones = intervaloIndices(arreglo, numeroQ)
    print(posiciones)

#-------------------------------------------------- EJERCICIO 4: Mapa de Romania --------------------------------------------------

# Construimos el mapa de Rumania como diccionario de adyacencias
def construirGrafo():
    grafo = {}
    grafo["Arad"] = [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)]
    grafo["Zerind"] = [("Arad", 75), ("Oradea", 71)]
    grafo["Oradea"] = [("Zerind", 71), ("Sibiu", 151)]
    grafo["Sibiu"] = [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)]
    grafo["Fagaras"] = [("Sibiu", 99), ("Bucharest", 211)]
    grafo["Rimnicu Vilcea"] = [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)]
    grafo["Pitesti"] = [("Rimnicu Vilcea", 97), ("Bucharest", 101), ("Craiova", 138)]
    grafo["Bucharest"] = [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)]
    grafo["Giurgiu"] = [("Bucharest", 90)]
    grafo["Urziceni"] = [("Bucharest", 85), ("Vaslui", 142), ("Hirsova", 98)]
    grafo["Vaslui"] = [("Urziceni", 142), ("Iasi", 92)]
    grafo["Iasi"] = [("Vaslui", 92), ("Neamt", 87)]
    grafo["Neamt"] = [("Iasi", 87)]
    grafo["Hirsova"] = [("Urziceni", 98), ("Eforie", 86)]
    grafo["Eforie"] = [("Hirsova", 86)]
    grafo["Timisoara"] = [("Arad", 118), ("Lugoj", 111)]
    grafo["Lugoj"] = [("Timisoara", 111), ("Mehadia", 70)]
    grafo["Mehadia"] = [("Lugoj", 70), ("Drobeta", 75)]
    grafo["Drobeta"] = [("Mehadia", 75), ("Craiova", 120)]
    grafo["Craiova"] = [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)]
    return grafo

#Usamos el algoritmo BFS para encontrar el camino con menos aristas
def bfsCamino(grafo, inicio, meta):
    visitados = set()
    cola = []
    #Diccionario que nos ayuda a recordar la ruta
    padres = {}
    cola.append(inicio)
    visitados.add(inicio)
    while len(cola) > 0:
        actual = cola.pop(0)
        if actual == meta:
            return reconstruir(padres, inicio, meta)
        vecinos = grafo.get(actual, [])
        i = 0
        while i < len(vecinos):
            vecino = vecinos[i][0]
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                cola.append(vecino)
            i = i + 1
    return []

# Reconstruye nuestro camino que guardamos en Padres (vamos de la meta al inicio e invertimos la lista)
def reconstruir(padres, inicio, meta):
    camino = []
    ciudad = meta
    while True:
        camino.append(ciudad)
        if ciudad == inicio:
            break
        ciudad = padres.get(ciudad, None)
        if ciudad is None:
            return []
    camino.reverse()
    return camino

# Convierte la hora ingresada por el usuario a minutos
def horaMinutos(horaTexto):
    horaTexto = horaTexto.strip()
    #Si la hora esta en HH:MM, la divimos en horas y minutos
    if ":" in horaTexto:
        partes = horaTexto.split(":")
        h = int(partes[0])
        m = int(partes[1])
        #obtenemos los minutos totales
        return h * 60 + m
    #si nos dan el numero de horas, unicamente la pasamos a minutos
    numero = float(horaTexto)
    h = int(numero)
    m = int(round((numero - h) * 60))
    return h * 60 + m

#Cambiamos nuestros minutos al formato HH:MM
def minutosHora(minutosAbs):
    minutosAbs = minutosAbs % 1440
    h = minutosAbs // 60
    m = minutosAbs % 60
    hTxt = str(h).rjust(2, "0")
    mTxt = str(m).rjust(2, "0")
    return hTxt + ":" + mTxt

#Definimos el comportamiento del tiempo segun los intervalos del dia
def factorPorHora(minutoAbs):
    t = minutoAbs % 1440
    if t < 360:
        return 1.0
    if t < 960:
        return 2.0
    return 1.5

#Esto es mas que nada para evitar usar fracciones de minutos (Segundos) si es que se llegan a presentar
def redondeo(x):
    entero = int(x)
    if x == entero:
        return entero
    return entero + 1

#Buscamos el tiempo que hay entre dos ciudades
def obtenerTiempo(grafo, a, b):
    vecinos = grafo.get(a, [])
    i = 0
    while i < len(vecinos):
        if vecinos[i][0] == b:
            return vecinos[i][1]
        i = i + 1
    return None

#Calculamos el tiempo sin considerar los intervalos del dia
def tiempoRecorrido(grafo, camino):
    total = 0
    i = 0
    while i < len(camino) - 1:
        a = camino[i]
        b = camino[i + 1]
        w = obtenerTiempo(grafo, a, b)
        total = total + w
        i = i + 1
    return total

#Calculamos el tiempo total considerando los intervalos del dia

def timepoTotal(grafo, camino, inicioAbs):
    baseTotal = tiempoRecorrido(grafo, camino)
    factor = factorPorHora(inicioAbs)
    totalReal = baseTotal * factor
    totalReal = redondeo(totalReal)
    llegadaAbs = inicioAbs + totalReal
    return totalReal, llegadaAbs


# Funcion principal: Le preguntamos al usuario los datos
def main():
    grafo = construirGrafo()
    print("Ciudades de Romania:")
    for nombre in sorted(grafo.keys()):
        print("-", nombre)
    origen = input("En que ciudad estas: ").strip()
    destino = input("A que ciudad quieres ir: ").strip()
    horaTexto = input("Cual es tu hora de salida (HH:MM o 13.5): ").strip()

    #Caso donde el usuario ingresa mal el nombre de una ciudad o una que no existe
    if origen not in grafo or destino not in grafo:
        print("Una ciudad no existe en el mapa")
        return

    salidaAbs = horaMinutos(horaTexto)
    camino = bfsCamino(grafo, origen, destino)

    #Consideramos que no es posible llegar entre las ciudades (muy poco probable)
    if len(camino) == 0:
        print("No hay camino entre las ciudades")
        return

    totalMin, llegadaAbs = timepoTotal(grafo, camino, salidaAbs)
    
    #Imprimimos el tiempo y el camino
    print("Camino elegido (BFS):", " -> ".join(camino))
    print("Tiempo total:", totalMin, "minutos")
    print("Hora estimada de llegada:", minutosHora(llegadaAbs))

if __name__ == "__main__":
    main()
    
