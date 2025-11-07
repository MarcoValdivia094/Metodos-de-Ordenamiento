def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        # Encuentra el índice del elemento más pequeño en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambia el elemento actual con el más pequeño encontrado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Ejemplo de uso
numeros = [64, 25, 12, 22, 11]
print("Antes de ordenar:", numeros)
selection_sort(numeros)
print("Después de ordenar:", numeros)
