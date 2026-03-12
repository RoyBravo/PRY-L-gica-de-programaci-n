"""
Programa de gestión de una lista de tareas.
Funciones:
- añadir tarea
- ver tareas
- eliminar tarea
"""

def mostrar_menu():
    print("\nGestor de tareas")
    print("1. Añadir alumno")
    print("2. Buscar alumno")
    print("3. Eliminar alumno")
    print("4. Salir")

def añadirAlumno(alumnos):
    nombre = input("Escribe el nombre del alumno: ")
    nota = input("Designe la nota del alumno: ")
    if nombre and nota:
        alumnos.append((nombre, nota))
        print(f"Alumno '{nombre}' con su nota '{nota}' fue añadido.")
    else:
        print("No se ha introducido el nombre del alumno.")
    
def buscarAlumno(alumnos):
    nombre = input("Escribe el nombre del alumno a buscar: ")
    for alumno in alumnos:
        if alumno[0] == nombre:
            print(f"Alumno encontrado: {alumno[0]} y su nota es{alumno[1]}")
            return
    print("Alumno no encontrado.")

def eliminarAlumno(alumnos):
    nombre = input("Escribe el nombre del alumno a eliminar: ")
    for i, alumno in enumerate(alumnos):
        if alumno[0] == nombre:
            alumnos.pop(i)
            print(f"Alumno '{nombre}' eliminado exitosamente.")
            return
    print("Alumno no encontrado.")
        
def main():
    alumnos = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            añadirAlumno(alumnos)
        elif opcion == "2":
            buscarAlumno(alumnos)
        elif opcion == "3":         
            eliminarAlumno(alumnos)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
