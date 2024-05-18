def check(a):
    if(len(a)<4): return False
    i=0
    while a[i+1]>a[i]:
         i+=1
    
    for x in range(i,len(a)-1):
        if a[x]<=a[x+1]: return False

    return True

      

t=int(input())
for _ in range(t):
    if(check(input().strip())): print("YES")
    else: print("NO")
