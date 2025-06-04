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