def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mueve los elementos de lista[0..i-1], que son mayores que clave,
        # una posición adelante de su posición actual
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

# Ejemplo de uso
numeros = [9, 3, 1, 5, 4]
print("Antes de ordenar:", numeros)
insertion_sort(numeros)
print("Después de ordenar:", numeros)

