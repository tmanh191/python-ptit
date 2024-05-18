m={1:1}
while True:
    a=[]
    check=1
    for i in m:
        if i<10**18:
            if not((i*2) in m):
                a.append(i*2)
            if not((i*3) in m):
                a.append(i*3)
            if not((i*5) in m):
                a.append(i*5)
    for i in a:
        check=0
        m[i]=1
    if check==1: break
a=sorted(list(m))
dem=1
for i in a:
    m[i]=dem
    dem+=1

t=int(input())
for i in range(t):
    n=int(input())
    if n in m: print(m[n])
    else: print("Not in sequence")
