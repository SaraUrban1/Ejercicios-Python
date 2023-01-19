def contador_palabras(texto):
    lista_texto = texto.split()
    dic_palabras = {}
    for i in lista_texto:
        if i in dic_palabras:
            dic_palabras[i] +=1
        else:
            dic_palabras[i] = 1
    return dic_palabras

print(contador_palabras("hola que tal hola"))

def palabra_top(dic_palabras):
    max_palabra = ''
    max_frecuencia = 0
    for palabra, freq in dic_palabras.items():
        if freq > max_frecuencia:
            max_palabra = palabra
            max_frecuencia=freq
    return max_palabra, max_frecuencia

print(palabra_top((contador_palabras("hola que tal que"))))

