dem=0
b=[0]*42
ar=[int(x) for x in input().split()]
for x in ar:
    b[x%42]=1
for x in b:
    if x> 0: dem+=1

print(dem)
