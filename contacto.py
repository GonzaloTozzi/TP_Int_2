class Contacto:
    #se crea el objeto contacto, con nombre, telefono y posicion izquierda y derecha para que se pueda armar el arbol binario
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.izquierda = None
        self.derecha = None