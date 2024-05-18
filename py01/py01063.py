def check(a,n):
    dem=0

    i=0
    while(i<=len(a)-len(n)):
        if a[i:i+len(n)]==n: 
            dem+=1
            i+=len(n)
        else: i+=1
    return dem

t=int(input())
for _ in range(t):
    a=input().strip()
    n=input().strip()

    print(check(a,n))