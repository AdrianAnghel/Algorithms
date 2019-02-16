import math
import statistics

n = int(input())
x = [int(i) for i in input().split()]

mean_x = statistics.mean(x)
sd = 0

for i in range(0, n):
    sd += (x[i] - mean_x) ** 2

print(round(math.sqrt(sd / n), 1))
