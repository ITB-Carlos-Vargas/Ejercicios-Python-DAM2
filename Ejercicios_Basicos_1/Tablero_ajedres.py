# Creacion de matriz en forma de tablero
def crear_tablero() -> list[list[str]]:
    tablero = []
    for fila in range(8):
        numeracion = 8 - fila #numeracion de la fila del tablero
        lista = []
        for columna in range(9):
            match columna:

                # Comprobar si se esta en la ultima columna
                case _ if columna == 8: 
                    lista.append(str(numeracion))
                # Marcar casilla blanca o negra si la suma de columna + fila es multiple de 2
                case _ if (columna + fila) % 2 == 0:
                    lista.append('O')
                case _:
                    lista.append('X')
        tablero.append(lista)
    # Agregar la "numeracion" de la filas
    tablero.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    return tablero
        
      
tablero = crear_tablero()
# Imprimir el tablero
for fila in tablero:
    print(" ".join(fila))
