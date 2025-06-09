class Contacto:
    #se crea la clase contacto, con nombre, telefono y posicion izquierda y derecha para que se pueda armar el arbol binario
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.izquierda = None
        self.derecha = None

def insertar(nodo_actual, nuevo_contacto):
    #si nodo actual is None, significa que encontro un lugar vacio para poder guardar el contacto dentro del arbol
    if nodo_actual is None:
        return nuevo_contacto
    #si el nuevo_contacto es menor alfabeticamente que el nodo actual se posiciona a la izquierda, si es mayor o igual a la derecha
    if nuevo_contacto.nombre.lower() < nodo_actual.nombre.lower():
        nodo_actual.izquierda = insertar(nodo_actual.izquierda, nuevo_contacto)
    else:
        nodo_actual.derecha = insertar(nodo_actual.derecha, nuevo_contacto)
    return nodo_actual

def buscar(nodo_actual, nombre_busqueda):
    #Si nodo actual is None significa que el contacto no esta en el arbol
    if nodo_actual is None:
        return None  
    if nombre_busqueda.lower() == nodo_actual.nombre.lower():
        return nodo_actual
    #si el nombre es menor, busca por el lado izquierdo, caso contrario busca por el lado derecho
    elif nombre_busqueda.lower() < nodo_actual.nombre.lower():
        return buscar(nodo_actual.izquierda, nombre_busqueda)
    else:
        return buscar(nodo_actual.derecha, nombre_busqueda)

def mostrar_contactos_en_orden(nodo_actual):
    if nodo_actual is not None:
        mostrar_contactos_en_orden(nodo_actual.izquierda)
        print(f"Nombre: {nodo_actual.nombre}, Teléfono: {nodo_actual.telefono}")
        mostrar_contactos_en_orden(nodo_actual.derecha)

def eliminar(nodo_actual, nombre):
    if nodo_actual is None:
        return None

    if nombre.lower() < nodo_actual.nombre.lower():
        nodo_actual.izquierda = eliminar(nodo_actual.izquierda, nombre)
    elif nombre.lower() > nodo_actual.nombre.lower():
        nodo_actual.derecha = eliminar(nodo_actual.derecha, nombre)
    else:
        if nodo_actual.izquierda is None:
            return nodo_actual.derecha
        elif nodo_actual.derecha is None:
            return nodo_actual.izquierda

        sucesor = encontrar_minimo(nodo_actual.derecha)
        nodo_actual.nombre = sucesor.nombre
        nodo_actual.telefono = sucesor.telefono
        nodo_actual.derecha = eliminar(nodo_actual.derecha, sucesor.nombre)

    return nodo_actual


def encontrar_minimo(nodo_actual):
    while nodo_actual.izquierda is not None:
        nodo_actual = nodo_actual.izquierda
    return nodo_actual

contactos_iniciales = [
    ("Ines", "1060"), ("Facundo", "1006"), ("Paula", "1042"), ("Gabriela", "1007"),
    ("Vanesa", "1047"), ("Wanda", "1048"), ("Kevin", "1037"), ("Nicolas", "1014"),
    ("Carlos", "1003"), ("Federico", "1057"), ("Florencia", "1032"), ("Tamara", "1045"),
    ("Olga", "1015"), ("Esteban", "1031"), ("Julieta", "1036"), ("Zaira", "1051"),
    ("Elena", "1005"), ("Camila", "1054"), ("Martina", "1039"), ("Leonardo", "1012"),
    ("Sofia", "1019"), ("Daniel", "1055"), ("Sebastian", "1044"), ("Isabel", "1009"),
    ("Pablo", "1016"), ("Helena", "1034"), ("Quimey", "1017"), ("Alina", "1052"),
    ("Ximena", "1024"), ("Rafael", "1043"), ("Jorge", "1010"), ("Agustina", "1027"),
    ("Lautaro", "1038"), ("Ana", "1001"), ("Gisela", "1058"), ("Dario", "1030"),
    ("Marina", "1013"), ("Raul", "1018"), ("Benjamin", "1028"), ("Uriel", "1046"),
    ("Julieta", "1036"), ("Zoe", "1026"), ("Iván", "1035"), ("Octavio", "1041"),
    ("Yamila", "1025"), ("Karen", "1011"), ("Xavier", "1049"), ("Ulises", "1021"),
    ("Cecilia", "1029"), ("Bruno", "1002"), ("Hugo", "1008"), ("Gonzalo", "1033"),
    ("Natalia", "1040"), ("Bautista", "1053"), ("Valeria", "1022"), ("Diego", "1004"),
    ("Rafael", "1043"), ("Tamara", "1045"), ("Yanina", "1050"), ("Emilia", "1056"),
    ("Horacio", "1059"), ("Alina", "1052")
]

def cargar_contactos_desde_lista(lista):
    raiz_del_arbol = None
    for nombre, telefono in lista:
        nuevo = Contacto(nombre, telefono)
        raiz_del_arbol = insertar(raiz_del_arbol, nuevo)
    return raiz_del_arbol



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
