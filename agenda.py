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
