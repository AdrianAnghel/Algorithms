# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = sorted(int(i) for i in input().split())


def median(arr):
    siz = len(arr)
    if siz % 2 == 0:
        return int(((arr[int(siz / 2) - 1] + arr[int(siz / 2)]) / 2))
    else:
        return int((arr[int(siz / 2)]))


print(median(x[0:n // 2]))
print(median(x))
if n % 2 == 0:
    print(median(x[n // 2:]))
else:
    print(median(x[n // 2 + 1:]))
