def merge(lista, inicio, medio, fin):
    izquierda = lista[inicio:medio+1]
    derecha = lista[medio+1:fin+1]
    i = j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

def straight_merging(lista):
    n = len(lista)
    bloque = 1
    while bloque < n:
        inicio = 0
        while inicio < n - bloque:
            medio = inicio + bloque - 1
            fin = min(inicio + 2 * bloque - 1, n - 1)
            merge(lista, inicio, medio, fin)
            inicio += 2 * bloque
        bloque *= 2

# Ejemplo de uso
datos = [34, 7, 23, 32, 5, 62]
print("Original:", datos)
straight_merging(datos)
print("Ordenados:", datos)
