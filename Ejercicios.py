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

#EJERCICO 2 CON PUNTO EXTRA 



