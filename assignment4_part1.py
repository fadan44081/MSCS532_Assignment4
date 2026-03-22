import random
import time

# -------------------------
# HEAPSORT
# -------------------------
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# -------------------------
# QUICKSORT
# -------------------------
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# -------------------------
# MERGE SORT
# -------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -------------------------
# PERFORMANCE TEST
# -------------------------
def test_sorting_algorithms():
    sizes = [1000, 5000, 10000]

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]

        print(f"\nArray size: {size}")

        # Heapsort
        heap_arr = arr.copy()
        start = time.time()
        heapsort(heap_arr)
        end = time.time()
        print(f"Heapsort time: {end - start:.5f} seconds")

        # Quicksort
        quick_arr = arr.copy()
        start = time.time()
        quicksort(quick_arr)
        end = time.time()
        print(f"Quicksort time: {end - start:.5f} seconds")

        # Merge Sort
        merge_arr = arr.copy()
        start = time.time()
        merge_sort(merge_arr)
        end = time.time()
        print(f"Merge Sort time: {end - start:.5f} seconds")


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    test_sorting_algorithms()