import math
def nto(a):
    a=int(a)
    for i in range(2,math.sqrt(a)+1):
        if a%i==0: return False
    return True

m,n=[int(x) for x in input().split()]

for i in range(n):
    a=[int(x) for x in input().split()]
    for i in a:
        if nto(i)==True: print(1,end=' ')
        else: print(0,end=" ")
    print()