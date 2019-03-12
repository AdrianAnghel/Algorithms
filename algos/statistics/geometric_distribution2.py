#a,b = [int(i) for i in input().split()]
#n = int(input())
a , b = [7, 10]
n=5
p = a/b
q = 1-p
print(round(sum(q**(i-1) * p for i in range(1,n+1)),3) )