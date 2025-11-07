def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso
datos = [10, 7, 8, 9, 1, 5]
print("Original:", datos)
ordenados = quicksort(datos)
print("Ordenados:", ordenados)
