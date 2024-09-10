# Insertion Sort com contagem de trocas
def insertion_sort(arr):
    n = len(arr)
    trocas = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            trocas += 1
            j -= 1
        arr[j + 1] = key
        if j + 1 != i:
            trocas += 1
    return arr, trocas

# Selection Sort com contagem de trocas
def selection_sort(arr):
    n = len(arr)
    trocas = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
    return arr, trocas

# Bubble Sort com contagem de trocas
def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
    return arr, trocas

# Vetor inicial
vetor = [20, 10, 50, 30, 40]

# Aplicando os algoritmos
insertion_sorted, insertion_trocas = insertion_sort(vetor.copy())
selection_sorted, selection_trocas = selection_sort(vetor.copy())
bubble_sorted, bubble_trocas = bubble_sort(vetor.copy())

# Exibindo os resultados com quebras de linha
print(f"Insertion Sort: {insertion_sorted}, Quantas trocas = {insertion_trocas}")
print(f"Selection Sort: {selection_sorted}, Quantas trocas = {selection_trocas}")
print(f"Bubble Sort: {bubble_sorted}, Quantas trocas = {bubble_trocas}")
