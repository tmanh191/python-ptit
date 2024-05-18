def check(a):
    a=int(a)
    if a<2: return False
    for x in range(2,int(a**0.5)+1):
        if a%x==0: return False
    return True

def hehe(a):
    if check(len(a))==False: return False
    sum=0
    for x in range(len(a)):
        if check(a[x])==True: sum+=1

    if sum<= len(a)-sum: return False

    return True
t=int(input())
for _ in range(t):
    a=input().strip()
   
    if(hehe(a) ): print("YES")
    else: print("NO")