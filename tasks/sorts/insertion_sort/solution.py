def insertion_sort(arr: list[int]) -> list[int]:
    a = arr[:]
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

solution = insertion_sort