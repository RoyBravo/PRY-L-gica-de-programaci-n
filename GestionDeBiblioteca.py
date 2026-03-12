"""
Gestion de biblioteca.
"""



def pedir_cadena(prompt: str) -> str:
    """Solicita al usuario una cadena no vacía; devuelve '' si pulsa Enter."""    
    return input(prompt).strip()

def mostrar_menu() -> None:
    print("\nGestor de biblioteca")
    print("1. Añadir libros (titulo, autor)")
    print("2. Ver listado de libros")
    print("3. Buscar libros por autor o título")
    print("4. Marcar libros como leidos")
    print("5. Salir")

def indice_por_titulo_o_autor(libros: list[tuple[str, str, bool]], texto: str) -> list[int]:
    """Devuelve los índices de los libros cuyo título o autor contiene el texto."""
    indices = []
    for i, (titulo, autor, leido) in enumerate(libros):
        if texto.lower() in titulo.lower() or texto.lower() in autor.lower():
            indices.append(i)
    return indices

def añadir_libro(libros: list[tuple[str, str, bool]]) -> None:
    titulo = pedir_cadena("Título del libro: ")
    if not titulo:
        print("Título vacío, operación cancelada.")
        return
    autor = pedir_cadena("Autor del libro: ")
    if not autor:
        print("Autor vacío, operación cancelada.")
        return
    libros.append((titulo, autor, False))
    print(f"Libro '{titulo}' de '{autor}' añadido.")

def ver_listado_libros(libros: list[tuple[str, str, bool]]) -> None:
    if not libros:
        print("No hay libros en la biblioteca.")
        return
    print("Listado de libros:")
    for titulo, autor, leido in libros:
        estado = " (leído)" if leido else ""
        print(f"  - {titulo} de {autor}{estado}")

def buscar_libros(libros: list[tuple[str, str, bool]]) -> None:
    texto = pedir_cadena("Introduce el texto a buscar: ")
    if not texto:
        print("Texto vacío, operación cancelada.")
        return
    indices = indice_por_titulo_o_autor(libros, texto)
    if not indices:
        print(f"No se encontraron libros con el texto '{texto}'.")
        return
    print(f"Libros encontrados con el texto '{texto}':")
    for i in indices:
        titulo, autor, leido = libros[i]
        estado = " (leído)" if leido else ""
        print(f"  - {titulo} de {autor}{estado}")

def marcar_como_leido(libros: list[tuple[str, str, bool]]) -> None:
    texto = pedir_cadena("Introduce el título o autor del libro a marcar como leído: ")
    if not texto:
        print("Texto vacío, operación cancelada.")
        return
    indices = indice_por_titulo_o_autor(libros, texto)
    if not indices:
        print(f"No se encontraron libros con el texto '{texto}'.")
        return
    for i in indices:
        titulo, autor, leido = libros[i]
        if not leido:
            libros[i] = (titulo, autor, True)
            print(f"Libro '{titulo}' de '{autor}' marcado como leído.")

def main() -> None:
    libros: list[tuple[str, str, bool]] = []
    while True:
        mostrar_menu()
        opcion = pedir_cadena("Selecciona una opción: ")
        if opcion == "1":
            añadir_libro(libros)
        elif opcion == "2":
            ver_listado_libros(libros)
        elif opcion == "3":
            buscar_libros(libros)
        elif opcion == "4":
            marcar_como_leido(libros)
        elif opcion == "5":
            print("Saliendo…")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
if __name__ == "__main__":
    main()