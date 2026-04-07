import time

def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

def fast_sort(arr):
    return sorted(arr)

def measure_time(sort_func, data, runs=5):
    times = []
    sorted_data = []
    
    for _ in range(runs):
        start_time = time.perf_counter()
        sorted_data = sort_func(data)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    return times, sorted_data

def main():
    data = []
    try:
        with open('arq.txt', 'r') as f:
            raw_data = f.read().split()
    except FileNotFoundError:
        print("Erro: Arquivo 'arq.txt' não encontrado na pasta atual.")
        return

    for item in raw_data:
        try:
            data.append(int(item))
        except ValueError:
            pass 

    if not data:
        print("Nenhum numero inteiro valido foi encontrado no arquivo.")
        return

    print(f"Total de numeros carregados: {len(data)}\n")

    print("Algoritmo: Bubble Sort")
    bubble_times, _ = measure_time(bubble_sort, data)
    for i, t in enumerate(bubble_times, 1):
        print(f"Execucao {i}: {t:.5f}s")
    
    media_bubble = sum(bubble_times) / len(bubble_times)
    print(f"Media: {media_bubble:.5f}s\n")

    print("Algoritmo: Quick Sort")
    fast_times, sorted_data = measure_time(fast_sort, data)
    for i, t in enumerate(fast_times, 1):
        print(f"Execucao {i}: {t:.5f}s")
        
    media_fast = sum(fast_times) / len(fast_times)
    print(f"Media: {media_fast:.5f}s\n")

    with open('arq-ordenado.txt', 'w') as f:
        f.write(' '.join(map(str, sorted_data)))
    print("Arquivo 'arq-ordenado.txt' gerado com sucesso!")

if __name__ == "__main__":
    main()