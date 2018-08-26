def missing_number(numbers_array):
    n = len(numbers_array) + 1
    missing_number = int(n * (n+1) / 2)
    for i in numbers_array:
        missing_number -= i
    return missing_number


print(missing_number([6,4,3,1,2]))
print(missing_number([1,2,3,4,5,6,7]))