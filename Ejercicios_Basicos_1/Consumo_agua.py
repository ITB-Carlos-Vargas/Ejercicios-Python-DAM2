# 1. Pedir cantidad de litros
litros = input("ingresa tu consumo de agua en litros: ")

# El proceso se repetira si se ingresa un valor invalido
valido = False
while not valido:

    # 2. validar el valor ingresado
    try:
        litros = int(litros)
    except ValueError:
        print("Por favor ingresa un número válido.")
        litros = input("ingresa tu consumo de agua en litros: ")
    
    # 3. Realizar el calculo de factura
    else:
        valido = True
        match litros:
            case _ if litros < 50:
                print("Factura total: 6€")
            case _ if litros >= 50 and litros < 200:
                print("Factura total: ", litros * 0.1, "€")
            case _ if litros >= 200:
                print("Factura total: ",litros * 0.3, "€")
            case _:
                print("No se puedo realizar la operacín correctamente.")
