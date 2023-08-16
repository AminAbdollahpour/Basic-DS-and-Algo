def insertion_sort(arr):
    for index in range(1, len(arr)):
        temp = arr[index]
        for element in range(0, index):
            if arr[element] > temp:
                arr[element], arr[index] = arr[index], arr[element]
    return arr

