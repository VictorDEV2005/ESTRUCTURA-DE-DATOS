class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Valor del nodo
        self.siguiente = None  # Referencia al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.head = None  # Referencia al primer nodo de la lista
        self.tamano = 0  # Mantener el tamaño de la lista

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.head:  # Si la lista está vacía, el nuevo nodo será la cabeza
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:  # Recorrer hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Enlazar el nuevo nodo al final
        self.tamano += 1

    def eliminar(self, valor):
        if not self.head:  # Si la lista está vacía
            return False
        
        if self.head.valor == valor:  # Si el valor a eliminar es el primero
            self.head = self.head.siguiente
            self.tamano -= 1
            return True
        
        actual = self.head
        while actual.siguiente:  # Recorrer la lista buscando el valor
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente  # Saltar el nodo que contiene el valor
                self.tamano -= 1
                return True
            actual = actual.siguiente
        return False  # Si el valor no se encontró

    def buscar(self, valor):
        actual = self.head
        while actual:
            if actual.valor == valor:
                return True  # Valor encontrado
            actual = actual.siguiente
        return False  # Valor no encontrado

    def longitud(self):
        return self.tamano  # Retorna el tamaño de la lista

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(actual.valor)  # Agregar cada valor a la lista de elementos
            actual = actual.siguiente
        return " -> ".join(map(str, elementos))  # Devolver una cadena de valores

    def recorrer(self):
        actual = self.head
        while actual:
            yield actual.valor  # Retorna un elemento a la vez
            actual = actual.siguiente
