def check(a):
    if len(a)%2==1: return False
    s=a[::-1]
    if a != s: return False
    for x in a:
        if int(x)%2!=0: return False
    
    return True

t=int(input())
for _ in range(t):
    a=int(input())
    for i in range(a):
        if(check(str(i))):
            print(i,end=' ')
    print()
