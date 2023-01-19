def frase_y_letra ():
    frase = input("Dime una frase")
    letra = input ("Elige una letra")
    contador = 0
    for cosa in frase:
        if cosa != letra:
            contador = contador
        elif cosa == letra:
            contador = contador + 1
    print (f"La letra {letra} aparece {contador}")

frase_y_letra()