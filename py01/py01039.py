def check(a):
    for i in range(2,len(a),2):
        if a[i]!=a[0] : return False
    
    for i in range(3,len(a),2):
        if(a[i]!=a[1]): return False
    
    if(a[1]==a[0]): return False

    return True

t=int(input())
for _ in range(t):
    if(check(input().strip())): print("YES")
    else: print("NO")