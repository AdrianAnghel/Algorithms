n = int(input())
x = [int(i) for i in input().split()]
# weight
w = [int(i) for i in input().split()]

su = 0
sd = 0

for i in range(0, n):
    su += x[i] * w[i]
    sd += w[i]

print(round(su / sd, 1))
