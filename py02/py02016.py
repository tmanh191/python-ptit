from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    m={}
    count=0
    for i in a:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    max=0
    for i in a:
        if m[i]>max:
            max=m[i]
            count=i
  
    if max>n/2: print(count)
    else: print("NO")
