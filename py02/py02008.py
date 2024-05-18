
sang=[True]*100000
sang[0]=sang[1]=False
for x in range(2,1000):
    if sang[x]==True:
        for i in range(x*x,100000,x):
            sang[i]=False

m={1:1}
a=[0]
dem=1
for x in range(10000):
    if sang[x]==True:
        a.append(x)
n,k=[int(x) for x in input().split()]
print(k,end=" ")
for i in range(n):
    k=k+a[i+1]
    print(k,end=' ')
        