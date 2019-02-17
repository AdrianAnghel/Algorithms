# Calculating the interquartile range of an array
# The first line contains an integer, n , denoting the number of elements in arrays  and .
# The second line contains n space-separated integers describing the respective elements of array .
# The third line contains n space-separated integers describing the respective elements of array .

def median(arr1):
    siz = len(arr1)
    if siz % 2 == 0:
        return int(((arr1[int(siz / 2) - 1] + arr1[int(siz / 2)]) / 2))
    else:
        return int((arr1[int(siz / 2)]))


n = int(input())
x = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]

# creating the new array based on frequencies
arr = []
for i in range(0, n):
    arr = arr + ([x[i]] * f[i])

# sorting the new array
arr.sort()

nn = len(arr)

# calculating Q1 and Q3
Q1 = median(arr[0:nn // 2])
if nn % 2 == 0:
    Q3 = median(arr[nn // 2:])
else:
    Q3 = (median(arr[nn // 2 + 1:]))

print(round(float(Q3 - Q1), 1))
