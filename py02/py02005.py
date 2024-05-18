t=int(input())
a=[int(x) for x in input().split()]
dem=0
for i in range(t-1):
    for j in range(i+1,t):
        if a[i]>a[j]: dem+=1

print(dem)