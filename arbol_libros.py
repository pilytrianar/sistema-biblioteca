class NodoLibro:
    def __init__(self, id_libro, titulo, autor, categoria, disponible=True):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = disponible
        self.izquierda = None
        self.derecha = None

class ArbolLibros:
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo, nuevo_libro):
        if nodo is None:
            return nuevo_libro
        if nuevo_libro.id < nodo.id:
            nodo.izquierda = self.insertar(nodo.izquierda, nuevo_libro)
        else:
            nodo.derecha = self.insertar(nodo.derecha, nuevo_libro)
        return nodo

    def buscar(self, nodo, id_libro):
        if nodo is None or nodo.id == id_libro:
            return nodo
        if id_libro < nodo.id:
            return self.buscar(nodo.izquierda, id_libro)
        return self.buscar(nodo.derecha, id_libro)

    def recorrer_inorden(self, nodo, resultado=[]):
        if nodo:
            self.recorrer_inorden(nodo.izquierda, resultado)
            resultado.append(nodo)
            self.recorrer_inorden(nodo.derecha, resultado)
        return resultado
