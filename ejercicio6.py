def las_matrices ():
    matriz1 = ((1,2,3),(4,5,6))
    matriz2 = ((-1, 0), (0,1), (1,1))
    filas_a = len(matriz1)
    filas_b = len(matriz2)
    columnas_a = len(matriz1[0])
    columnas_b = len(matriz2[0])
    lista_a_mostrar = []
    #recorre las filas de la segunda matriz
    for a in range(filas_b):
        lista_a_mostrar.append([])
        for b in range(columnas_b):
            lista_a_mostrar[a].append(None)
    #ahora las columnas
    for c in range(columnas_b):
        for d in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += matriz1[d][j] * matriz2[j][c]
            lista_a_mostrar[d][c] = suma
    return lista_a_mostrar

print(las_matrices())