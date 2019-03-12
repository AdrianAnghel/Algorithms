#a,b = [int(i) for i in input().split()]
#n = int(input())
a , b = [7, 10]
n=5
p = a/b
q = 1-p
print(round(q**(n-1) * p,3))