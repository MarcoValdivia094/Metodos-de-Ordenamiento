def distribute_runs_polyphase(runs):
    """
    Distribuye los runs entre tres archivos simulados para Polyphase Sort.
    """
    A, B, C = [], [], []
    total_runs = len(runs)
    # Distribución inicial: Fibonacci inverso (ejemplo simple)
    A = runs[:total_runs // 2]
    B = runs[total_runs // 2:]
    return A, B, C

def polyphase_merge(A, B, C):
    """
    Simula el proceso de mezcla Polyphase con tres archivos.
    """
    result = []
    while A or B:
        merged = []
        if A and B:
            merged = merge_runs(A.pop(0), B.pop(0))
        elif A:
            merged = A.pop(0)
        elif B:
            merged = B.pop(0)
        result.append(merged)
        C.append(merged)  # Archivo de salida temporal

        # Rotación de archivos
        A, B, C = B, C, []

    return result[-1] if result else []

def merge_runs(run1, run2):
    """
    Mezcla dos runs ordenados.
    """
    i = j = 0
    merged = []
    while i < len(run1) and j < len(run2):
        if run1[i] < run2[j]:
            merged.append(run1[i])
            i += 1
        else:
            merged.append(run2[j])
            j += 1
    merged.extend(run1[i:])
    merged.extend(run2[j:])
    return merged

# Ejemplo de uso
runs = [
    [1, 4], [2, 5], [3, 6], [7, 8]
]

A, B, C = distribute_runs_polyphase(runs)
sorted_result = polyphase_merge(A, B, C)
print("Resultado ordenado:", sorted_result)
