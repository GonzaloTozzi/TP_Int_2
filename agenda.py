from funciones import insertar, buscar, eliminar, mostrar_contactos_en_orden,cargar_contactos_desde_lista
from contacto import Contacto
from lista_contactos_inicial import contactos_iniciales

def menu():
    nodo_raiz = cargar_contactos_desde_lista(contactos_iniciales)

    while True:
        print("\n--- Menú de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            if buscar(nodo_raiz, nombre):
                print("Ya existe un contacto con ese nombre")
            else:
                telefono = input("Teléfono: ")
                nuevo = Contacto(nombre, telefono)
                nodo_raiz = insertar(nodo_raiz, nuevo)
                print("\nContacto agregado.")

        elif opcion == "2":
            nombre = input("Nombre del contacto a buscar: ")
            encontrado = buscar(nodo_raiz, nombre)
            if encontrado:
                print(f"Contacto encontrado: {encontrado.nombre}, Teléfono: {encontrado.telefono}")
            else:
                print("\nContacto no encontrado.")

        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            nodo_raiz = eliminar(nodo_raiz, nombre)
            print("\nContacto eliminado.")

        elif opcion == "4":
            print("\nLista de contactos:")
            mostrar_contactos_en_orden(nodo_raiz)

        elif opcion == "5":
            print("\nSaliendo del programa.")
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.")


menu()
