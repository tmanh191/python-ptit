
def chh(a):  
    if(len(a)<4): return False
    i=0
    while a[i]<a[i+1]: i+=1
    for j in range(i,len(a)-1):
        if a[j]<=a[j+1]: return False

    return True


n=int(input())
for _ in range(n):
    a=input().strip()
    if chh(a): print("YES")
    else: print("NO")