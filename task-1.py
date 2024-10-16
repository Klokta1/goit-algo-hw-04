import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def tim_sort(arr):
    return sorted(arr)

def generate_data(size):
    return [random.randint(1, 10000) for _ in range(size)]

def generate_sorted_data(size):
    return list(range(size))

def generate_reverse_sorted_data(size):
    return list(range(size, 0, -1))

def measure_time(algorithm, data):
    return timeit.timeit(lambda: algorithm(data.copy()), number=1)

if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    algorithms = [merge_sort, insertion_sort, tim_sort]
    data_types = {
        "Random": generate_data,
        "Sorted": generate_sorted_data,
        "Reversed": generate_reverse_sorted_data
    }

    for size in sizes:
        print(f"\nData Size: {size}")
        for data_type, data_func in data_types.items():
            print(f"  Data Type: {data_type}")
            data = data_func(size)
            for algorithm in algorithms:
                time_taken = measure_time(algorithm, data)
                print(f"    {algorithm.__name__}: {time_taken:.6f} seconds")
