
n=int(input())
a=[[[0]*n] for i in range(n)]
for i in range(n):
    a[i]=[int(x) for x in input().split()]

duoi=0
tren=0
for i in range(n):
    for j in range(n):
        if i+j<n-1:
            tren+=a[i][j]
        
        if i+j>=n:
            duoi+=a[i][j]

k=int(input())
if k<abs(tren-duoi): print("NO")
else: print("YES")

print(abs(tren-duoi))