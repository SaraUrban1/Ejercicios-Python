def vectores ():
    a = (1,2,3)
    b = (-1, 0, 2)
    lista= []
    for i in a:
        producto = a[i-1]*b[i-1]
        lista.append(producto)
    print(f"El producto de los vectores {a} y {b} es {lista}") #lalalal



vectores()