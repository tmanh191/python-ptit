def check(a):
    for i in range(0,len(a)):
        if a[i]!='0' and a[i]!='1' and a[i]!='2':
            return False
        
    return True

t=int(input())
for _ in range(t):
    if(check(input().strip())): print("YES")
    else: print("NO")
