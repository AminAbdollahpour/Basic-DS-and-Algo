def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        midpoint = (len(arr)) // 2
        if arr[midpoint] == target:
            return True
        else:
            if arr[midpoint] < target:
                return recursive_binary_search(arr[midpoint + 1:], target)
            else:
                return recursive_binary_search(arr[:midpoint], target)


def verify(result):
    print('Target ', result)


collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(collection, 6)
verify(result)
