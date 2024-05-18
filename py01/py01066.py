def check(a):
    b=a[::-1]

    for x in range(1,len(a)):
        if abs( ord(a[x])-ord(a[x-1]) )!=abs( ord(b[x])-ord(b[x-1]) ):
            return False
    return True

t=int(input())
for _ in range(t):
    a=input().strip()
    if(check(a)): print("YES")
    else: print("NO")