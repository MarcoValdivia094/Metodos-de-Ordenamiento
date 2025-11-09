def fibonacci_distribution(total_runs):
    """
    Calcula la distribución inicial de runs según la secuencia de Fibonacci.
    Devuelve una tupla con la cantidad de runs en cada archivo.
    """
    fib = [1, 1]
    while sum(fib) < total_runs:
        fib.append(fib[-1] + fib[-2])

    # Ajustamos para que la suma sea igual a total_runs
    while sum(fib[:-1]) >= total_runs:
        fib.pop()

    # Distribución: los dos primeros archivos reciben fib[-2] y fib[-3] runs
    return fib[-2], fib[-3], 0  # Archivo de salida empieza vacío

# Ejemplo de uso
total_runs = 13
A_runs, B_runs, C_runs = fibonacci_distribution(total_runs)
print(f"Distribución inicial de runs:\nA: {A_runs}, B: {B_runs}, C: {C_runs}")
