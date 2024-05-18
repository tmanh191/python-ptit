t=int(input())
a=[int(x) for x in input().split()]
tam=a[0]
dem=0
for x in range(1,t):
   
    if a[x]!=tam: dem+=1
    
    tam=a[x]

print(dem)