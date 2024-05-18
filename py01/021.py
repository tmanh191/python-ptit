

t=int(input())
for _ in range(t):
    li=[]
    a=input().strip()
    sum=0
    for i in a:
        s=""+i
        if ord(s)>64 and ord(s)<92: li.append(i)
        else:
            sum+=int(i)
    
    li=sorted(li)
    for i in li:
        print(i,end='')
    print(sum)