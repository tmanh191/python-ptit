def c(a):
   
    a=int(a)
    if a<2: return False
    for x in range(2,int(a**0.5)+1):
        if(a%x==0): return False

    return True

def nt(a):
    for x in range(len(a)):
        if c(x)==True:
            if c(a[x])==False: return False
        else:
            if c(a[x])==True: return False

    return True

t=int(input())
for _ in range(t):
    if(nt(input().strip())): print("YES")
    else: print("NO")
