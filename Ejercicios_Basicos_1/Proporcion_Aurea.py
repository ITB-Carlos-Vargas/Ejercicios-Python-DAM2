# Funcion recursiva que imprime el numero aureo 
def secuencia_aurea(segmento: int, anterior: int, actual: int):
    print(actual)
    segmento-=1
    siguiente = anterior+actual
    if not segmento == 0:
        secuencia_aurea(segmento,actual, siguiente)

valido = False 
while not valido:
    eleccion = input("Ingrese la cantidad de valores aureos que desea visualizar: ")
    try:
        eleccion = int(eleccion)
    except:
        print("Ingrese un numero valido")
    else:
        valido = True
        secuencia_aurea(eleccion, 0, 1)