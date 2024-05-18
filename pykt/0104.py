so='1234567890'

t=int(input())
for i in range(t):
    te=input().strip()
    re=''
    for i in te:
        if i not in so:
            re+=" "
        else:
            re+=i
        
    lis=re.split()
    minn=-100000000
    for i in lis:
        if int(i)>minn:
            minn=int(i)

    print(minn)