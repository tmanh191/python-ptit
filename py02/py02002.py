mang=[0,1,1]
p1=1
p2=1
for i in range(3,93):
    k=p1+p2
    mang=mang+[k]
    p1=p2
    p2=k

t=int(input())
for i in range(t):
    n,k=[int(x) for x in input().split()]
    for e in range(n,k+1):
        print(mang[e],end=" ")
    print()