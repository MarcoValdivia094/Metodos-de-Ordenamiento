import heapq

def balanced_multiway_merge(sorted_runs):
    """
    Realiza una mezcla equilibrada multivía de listas ordenadas.
    :param sorted_runs: Lista de listas ordenadas (runs).
    :return: Lista ordenada final.
    """
    heap = []
    result = []

    # Inicializa el heap con el primer elemento de cada run
    for i, run in enumerate(sorted_runs):
        if run:
            heapq.heappush(heap, (run[0], i, 0))  # (valor, índice de run, índice interno)

    while heap:
        value, run_idx, elem_idx = heapq.heappop(heap)
        result.append(value)

        # Si hay más elementos en el mismo run, agrégalos al heap
        if elem_idx + 1 < len(sorted_runs[run_idx]):
            next_value = sorted_runs[run_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, run_idx, elem_idx + 1))

    return result

# Ejemplo de uso
runs = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11]
]

merged = balanced_multiway_merge(runs)
print("Resultado ordenado:", merged)
