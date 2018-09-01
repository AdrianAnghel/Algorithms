def sort_one_two(arr):
    i = 0
    mid = 0
    j = len(arr) - 1

    while mid <= j:

        if arr[mid] > arr[j]:
            arr[mid], arr[j] = arr[j], arr[mid]

        if arr[i] > arr[mid]:
            arr[i], arr[mid] = arr[mid], arr[i]

        mid += 1

        while arr[j] == 2:
            j -= 1
        while arr[i] == 0:
            i += 1
            mid = i

    print(str(i) + ' ' + str(mid) + ' ' + str(j))
    return arr


arr1 = [2, 0, 0, 1, 2, 0, 1, 0]

print(sort_one_two(arr1))

arr2 = [2, 0, 0, 1, 2, 0, 1, 0, 1, 1, 2, 1, 1, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0]

print(sort_one_two(arr2))

arr3 = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

print(sort_one_two(arr3))

arr4 = [1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2]

print(sort_one_two(arr4))

arr5 = [2, 2, 1, 0]

print(sort_one_two(arr5))
