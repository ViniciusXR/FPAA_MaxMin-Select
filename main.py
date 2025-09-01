def maxmin_select(arr, low, high):
    """
    Algoritmo de seleção simultânea (MaxMin Select) usando divisão e conquista.
    
    Args:
        arr: Lista de números
        low: Índice inicial do subarray
        high: Índice final do subarray
    
    Returns:
        tupla (min, max) contendo o menor e maior elemento do subarray
    """
    # Caso base 1: apenas um elemento
    if low == high:
        return arr[low], arr[low]
    
    # Caso base 2: dois elementos
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # Caso geral: dividir o array
    mid = (low + high) // 2
    
    # Conquista: resolver recursivamente os subproblemas
    min1, max1 = maxmin_select(arr, low, mid)
    min2, max2 = maxmin_select(arr, mid + 1, high)
    
    # Combinar os resultados
    overall_min = min(min1, min2)
    overall_max = max(max1, max2)
    
    return overall_min, overall_max


def test_maxmin():
    """
    Função para testar o algoritmo MaxMin Select.
    """
    # Casos de teste
    test_cases = [
        [5, 2, 8, 1, 9, 3],
        [10],
        [3, 7],
        [9, 4, 2, 1, 8, 5, 6, 3, 7],
        [-5, -2, -8, -1, -9, -3]
    ]
    
    print("=== Teste do Algoritmo MaxMin Select ===\n")
    
    for i, arr in enumerate(test_cases, 1):
        min_val, max_val = maxmin_select(arr, 0, len(arr) - 1)
        print(f"Array {i}: {arr}")
        print(f"Mínimo: {min_val}, Máximo: {max_val}\n")


if __name__ == "__main__":
    test_maxmin()