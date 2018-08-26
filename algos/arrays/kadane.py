'''
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''


def kadane(numbers):
    current_max = new_max = numbers[0]
    for number in numbers[1:]:
        current_max = max(number, current_max + number)
        new_max = max(current_max, new_max)
    return new_max

""""
def read_testcase(test_case):
    for i in range(0, test_case):
        n = int(input())
        numbers = [int(x) for x in input().split()]
        print("Max sum of array is " + str(kadane(n, numbers)))



test_cases = int(input())

read_testcase(test_cases)
"""

print(kadane([1, 2, 10]))
print(kadane([-1, -2, -3, -4]))
print(kadane([5, -6, 0, 1, 3 , -3, 7]))
