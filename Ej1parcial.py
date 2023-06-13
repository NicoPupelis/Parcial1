def contar_palabra(palabra, vector):
    if not vector:
        return 0
    else:
        if vector[0] == palabra:
            return 1 + contar_palabra(palabra, vector[1:])
        else:
            return contar_palabra(palabra, vector[1:])


palabras = ["hola", "mundo", "hola", "amigo", "hola"]
palabra = "hola"

resultado = contar_palabra(palabra, palabras)
print("La palabra", palabra, "aparece", resultado, "veces en el vector.")
