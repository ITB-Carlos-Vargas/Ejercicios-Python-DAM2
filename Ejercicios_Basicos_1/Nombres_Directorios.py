from pathlib import Path
import re

def main():
    # 1. Pedir al usuario la ruta del directorio
    ruta = input("Introduce la ruta del directorio donde están los archivos: ").strip()
    directorio = Path(ruta)

    # Validar si el directorio existe
    if not directorio.exists() or not directorio.is_dir():
        print("Error: el directorio no existe.")
        return

    # 2. Pedir el patrón y el texto de reemplazo
    patron = input("Introduce el patrón (expresión regular) a buscar: ").strip()
    reemplazo = input("Introduce el texto de reemplazo: ").strip()

    # 3. Recorrer los archivos del directorio
    for archivo in directorio.iterdir():
        if archivo.is_file():  # solo archivos, no carpetas
            nombre_original = archivo.name

            # 4. Aplicar la expresión regular
            nuevo_nombre = re.sub(patron, reemplazo, nombre_original)

            # 5. Renombrar si el nombre cambió
            if nuevo_nombre != nombre_original:
                archivo.rename(archivo.with_name(nuevo_nombre))
                print(f"Renombrado: {nombre_original} → {nuevo_nombre}")

    print("Proceso completado.")


main()
