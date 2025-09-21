# proceso para seleccionar un numero dentro de una lista especifica
def control_seleccionador(mensaje: str, error: str, limite: int) -> int:
    valido = False
    eleccion = input(mensaje)
    while not valido:
        try:
            eleccion = int(eleccion) 
        except ValueError:
            print(error)
            eleccion = input(mensaje)
        else:
            if(eleccion <= limite):
                eleccion-=1
                valido = True
                return eleccion
            else:
                print(error)
                eleccion = input(mensaje)

# Proceso para controlar el pago, efectivo y el cambio
def control_pago(monto: float, efectivo: list) -> bool:
    total = 0.0
    print ("Por favor realize el pago")

    # El proceso no terminara hasta que el total ingresado sea igual o supere al monto
    while total < monto:
        print(f"Total: {round(monto - total, 2)}")
        pago = input("Ingrese la cantidad a pagar: ")

        # Validar que haya ingresado un numero valido
        try:
            pago = float(pago)
        except ValueError:
            print("Ingrese un valor valido")

            # Verificar que la cantidad ingresada este en sistema efectivo
        else:
            if pago in efectivo:
                total += pago
            else:
                print("Solo efectivo valido")
    if total == monto:
        print("Pago realizado")
        
        #Mostrar la cantidad de cambien si el pago supera al monto
    if total > monto:
        print(f"Pago realizado\nSu vuelto es de {round(total - monto, 2)}")
    return True


billetes = {
    "Billete sencillo": 2.2, 
    "Tcasual": 10.2,
    "Tmes": 54,
    "TTrismete" : 145.3,
    "Tjoven" : 105
}

zonas = {
    "zona 1": 1,
    "zona 2": 1.35,
    "zona 3": 1.89
}

efectivo = [
    0.01, 0.02, 0.05,
    0.10, 0.20, 0.50,
    1, 2,
    5, 10, 20, 50,
    100, 200, 500
]

repeticion = True
while repeticion:
    #  1. Mostrar los billetes y selecionar uno
    index = 0
    for x in billetes:
        index+=1
        print(index, x)
    eleccion_billete = control_seleccionador("Elige el numero del billete que deseas comprar: ", "Ingrese un numero valido", len(billetes) )
    
    # 2. Tomar los valores de la zona y los billetes
    precios = list(billetes.values())
    multiplicador = list(zonas.values())

    # 3. Mostrar las zonas y selecionar una
    print("zonas disponibles")
    for x in zonas:
        print(x)
    eleccion_zona =control_seleccionador("Ingresa el numero de la zona deseada: ", "ingrese una zona valida: ", len(zonas))
    
    # 4. Calcular el total a pagar y realizar el proceso de pago
    total = round(precios[eleccion_billete] * multiplicador[eleccion_zona], 2)
    control_pago(total, efectivo)

    # 5. Control de repetecion de proceso
    eleccion_repet = input ("desea realizar otra operacion?\nConfirmar:oprima y: ")
    if not eleccion_repet == "y" or eleccion_repet =="Y":
        print ("gracias por su compra")
        repeticion = False
