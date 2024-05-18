import math
def nto(a):
    a=int(a)
    if a<2: return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0: return False
    return True

n=int(input())
for _ in range(n):
    a=int(input())
    sum=0
    for i in range(1,a):
        if math.gcd(a,i)==1: sum+=1
  
    if nto(sum)==True: print("YES")
    else: print("NO")