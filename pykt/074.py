


t=int(input())

for _ in range(t):
    text=input().strip().split()
    res=''

    for i in text:
        if len(res)+len(i)>100: break

        res+=i+' '

    print(res.strip())


