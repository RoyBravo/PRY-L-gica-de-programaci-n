"""
Programa de gestión de una lista de tareas.
Funciones:
- añadir tarea
- ver tareas
- eliminar tarea
"""

def mostrar_menu():
    print("\nGestor de tareas")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")


def añadir_tarea(tareas):
    tarea = input("Escribe la tarea: ")
    if tarea:
        tareas.append(tarea)
        print(f"Tarea '{tarea}' añadida.")
    else:
        print("No se ha introducido ninguna tarea.")


def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
        return
    print("\nLista de tareas:")
    for i, t in enumerate(tareas, start=1):
        print(f"{i}. {t}")


def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas que eliminar.")
        return
    ver_tareas(tareas)
    try:
        indice = int(input("Número de la tarea a eliminar: "))
        if 1 <= indice <= len(tareas):
            tarea = tareas.pop(indice - 1)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debe introducir un número.")


def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            añadir_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
