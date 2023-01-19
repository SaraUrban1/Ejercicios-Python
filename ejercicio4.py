def contrasena ():
    modelo = "12345EDD"
    pregunta = input("Dime tu contraseña")
    while pregunta != modelo:
        print ("Vuelve a intentarlo")
        pregunta = input("Dime tu contraseña")
        if modelo == pregunta:
            print("Es correcto")
            break
    if pregunta == modelo:
        print ("Es correcto")

contrasena()