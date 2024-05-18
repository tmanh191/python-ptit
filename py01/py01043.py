def check(a):
    if len(a)%2!=0 : return False

    for x in range(0,len(a)):
        if int(a[x])%2!=0: return False
    
    if(a!=a[::-1]): return False

    return True

t=int(input())
for _ in range(t):
    a=int(input())
    for x in range(22,a,22):
        if(check(str(x))): print(x,end=' ')

    print()
