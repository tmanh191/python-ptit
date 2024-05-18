import math
def snt(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False

    return True

t=int(input())

for _ in range(t):
    a=input()
    stringa=a.split()
    x=int(stringa[0])
    y=int(stringa[1])
    
    c=str(math.gcd(x,y))
    dem=0
    for x in c:
        dem+=int(x)
    
    if snt(dem):
        print("YES")
    else:
        print("NO")

