transiciones = {1:{'-':2, '+':2, 'dd':3}, 2:{'dd':3}, 3:{'dd':3}}
aceptacion = {3}


def convertidor(caracter):
    retorno = ""
    if caracter.isdigit():
        retorno = 'dd'
    else:
        retorno = caracter
    return retorno

def analizador(cadena):
    estado_actual = 1
    lexema = ""
    for c in cadena:
        transiciones_posibles = transiciones[estado_actual]
        try:
            estado_actual = transiciones_posibles[convertidor(c)]
            lexema = lexema + c
        except KeyError:
            #Acá validar si estoy en aceptación
            if estado_actual in aceptacion:
                print("Se reconoce la palabra", lexema)
            estado_actual = 1
            lexema = ""
    if estado_actual in aceptacion:
        print("Se reconoce la palabra", lexema)

oracion = "Todos los alumnos -90 de progra 2 sacaron -1 en su examen parcial 1"
analizador(oracion)