def find_runs(arr):
    """
    Encuentra secuencias ordenadas (runs) naturales en el arreglo.
    Devuelve una lista de sublistas, cada una siendo una secuencia ordenada.
    """
    runs = []
    run = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            run.append(arr[i])
        else:
            runs.append(run)
            run = [arr[i]]
    runs.append(run)
    return runs

def merge(left, right):
    """
    Fusiona dos listas ordenadas en una sola lista ordenada.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def natural_merge_sort(arr):
    """
    Aplica el algoritmo de Natural Merging:
    1. Encuentra secuencias ordenadas naturales.
    2. Fusiona secuencias hasta que quede una sola lista ordenada.
    """
    while True:
        runs = find_runs(arr)
        if len(runs) == 1:
            # Ya está completamente ordenado
            break
        new_arr = []
        # Fusiona pares de secuencias
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged = merge(runs[i], runs[i + 1])
            else:
                merged = runs[i]
            new_arr.extend(merged)
        arr = new_arr
    return arr

data = [5, 7, 8, 1, 2, 3, 9, 4, 6]
sorted_data = natural_merge_sort(data)
print(sorted_data)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
