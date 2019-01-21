
def bubbleSort(arr):
    # Bubble sorting: swap adjacent values, loop through the list until none is swapped

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr

arr = list(map(int, input().split(' ')))
print(bubbleSort(arr))
