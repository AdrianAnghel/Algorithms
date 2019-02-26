# Enter your code here. Read input from STDIN. Print output to STDOUT

d_pct, n = 12, 10


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def odds(pcnt):
    return pcnt / 100, (100 - pcnt) / 100


def combination(n, k):
    return factorial(n) / (factorial(k) * (factorial(n - k)))


def binomial(n, x, p, q):
    return combination(n, x) * p ** x * q ** (n - x)


first_result = 0
second_result = 0

p, q = odds(d_pct)
for i in range(0, 3):
    first_result += binomial(n, i, p, q)

for i in range(2, n + 1):
    second_result += binomial(n, i, p, q)

print(round(first_result, 3))
print(round(second_result, 3))
