def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Ordena recursivamente ambas mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Combina las mitades ordenadas
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Agrega los elementos restantes
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
datos = [38, 27, 43, 3, 9, 82, 10]
print("Original:", datos)
merge_sort(datos)
print("Ordenados:", datos)
