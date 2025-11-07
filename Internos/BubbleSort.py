def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambia si el elemento actual es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ejemplo de uso
numeros = [5, 1, 4, 2, 8]
print("Antes de ordenar:", numeros)
bubble_sort(numeros)
print("Después de ordenar:", numeros)
