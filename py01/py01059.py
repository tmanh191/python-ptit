def check(a):
    for x in range(len(a)):
        if x%2==1:
            if a[x]!='0': return False

    return True

t=int(input())
for _ in range(t):
    a=input().strip()
    sum=0
    tich=1
    for x in range(len(a)):
        if x%2==0:
            sum+=int(a[x])
        else:
            if a[x]!='0':
                tich*=int(a[x])
    
    if(check(a)==True): tich=0

    print(sum," ",tich)