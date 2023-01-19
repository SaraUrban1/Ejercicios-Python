def numeritos ():
    listita = [50, 75, 46, 22, 80, 65, 8]
    mayor = 0
    menor = 8
    for numero in listita:
        if numero > mayor:
            mayor = numero
    for numero in listita:
        if numero < menor:
            menor = numero
    print (mayor, menor)

numeritos()