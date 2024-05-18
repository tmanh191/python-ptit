t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted([int(x) for x in input().split()])
    b=sorted([int(x) for x in input().split()])
    ok=True
    for i in range(n):
        if a[i]>b[i]: 
            
            ok=False
            break
    
    if ok: print("YES")
    else: print("NO")
