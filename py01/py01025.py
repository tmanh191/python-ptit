a=input()
res=''
dem=0
for x in a[::-1]:
    dem+=1
    res+=x
    if dem%3==0 and dem< len(a): res+=','

print(res[::-1])
