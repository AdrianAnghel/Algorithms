# Enter your code here. Read input from STDIN. Print output to STDOUT
n=6
p, q = [1.09, 1]

m=p/(p+q)
f=q/(p+q)

def factorial(n):
    if n>1:
        return n * factorial(n-1)
    else:
        return 1

def combination(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))


def binomial(n,x,m,f):
    return combination(n,x) * (m**x) * (f**(n-x))


sum=0
for i in range(3,7):
    sum+=binomial(n,i,m,f)

print(round(sum,3))
