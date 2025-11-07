# Definición del nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para insertar un valor en el BST
def insertar(root, valor):
    if root is None:
        return Nodo(valor)
    if valor < root.valor:
        root.izquierda = insertar(root.izquierda, valor)
    else:
        root.derecha = insertar(root.derecha, valor)
    return root

# Recorrido in-order para obtener los elementos ordenados
def recorrido_inorder(root, resultado):
    if root:
        recorrido_inorder(root.izquierda, resultado)
        resultado.append(root.valor)
        recorrido_inorder(root.derecha, resultado)

# Función principal de Tree Sort
def tree_sort(lista):
    root = None
    for valor in lista:
        root = insertar(root, valor)
    resultado = []
    recorrido_inorder(root, resultado)
    return resultado

# Ejemplo de uso
datos = [5, 3, 7, 2, 4, 6, 8]
print("Original:", datos)
ordenados = tree_sort(datos)
print("Ordenados:", ordenados)
