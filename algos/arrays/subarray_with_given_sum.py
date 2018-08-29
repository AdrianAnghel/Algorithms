"""
https://www.geeksforgeeks.org/find-subarray-with-given-sum/
Given an unsorted array of non-negative integers,
find a continuous sub-array which adds to a given number. First element in array is 1.
"""


def find_subarray_with_sum(arr, desired_sum):
    arr_size = len(arr)
    start = 0
    sum_so_far = arr[0]
    i = 1

    while i <= arr_size:

        # Sum so far is bigger than the desired sum
        # Removing the first elements ono by one
        # until sum so far is less or equal to desired sum
        while sum_so_far > desired_sum and start < i - 1:
            sum_so_far -= arr[start]
            start += 1

        # Found the desired sum
        # start needs to be incremented by one because the array started from 0
        # i was already incremented last round
        if sum_so_far == desired_sum:
            return start + 1, i

        if i < arr_size:
            sum_so_far += arr[i]

        i += 1

    return -1


arr1 = [1, 2, 3, 7, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr3 = [10, 3, 4]

# print(find_subarray_with_sum(arr1, 12))
# print(find_subarray_with_sum(arr2, 15))
# print(find_subarray_with_sum(arr2, 10))
# print(find_subarray_with_sum(arr2, 55))
# print(find_subarray_with_sum(arr2, 56))
print(find_subarray_with_sum(arr3, 7))
