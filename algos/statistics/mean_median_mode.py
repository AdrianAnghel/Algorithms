n = int(input())
x = sorted(int(i) for i in input().split())

print(sum(x) / n)
if n % 2 == 0:
    print((x[int(n / 2) - 1] + x[int(n / 2)]) / 2)
else:
    print((x[int(n / 2)]))
print(max(x, key=x.count))
