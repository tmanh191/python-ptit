def check(a):
    if len(a)>4:
        a=a[len(a)-4:len(a)]
    
    a=int(a)
    if a<2: return False
    for x in range(2,int(a**0.5)+1):
        if(a%x==0): return False

    return True

t=int(input())
for _ in range(t):
    if(check(input().strip())): print("YES")
    else: print("NO")
