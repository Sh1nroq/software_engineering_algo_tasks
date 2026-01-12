def bubble_sort(arr: list[int]) -> list[list[int]]:
    n = len(arr)
    snapshots = []
    arr = arr[:]

    for i in range(n):
        swapped = False

        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped:
            snapshots.append(arr[:])

        else:
            if i == 0:
                snapshots.append(arr[:])
            break

    return snapshots

solution = bubble_sort