
n=int(input())
a=[]
for _ in range(n):
    a.append(input().strip())

s=''
for i in a:
    s=s+str(len(i.split()))

tho=''
for i in s:
    if i=="6" or i=='8':
        tho=tho+'1'
    else:
        tho=tho+'7'
# print(tho)
kq=''
dem=0
for i in range(0,len(tho)):
    if tho[i]=='1' and tho[i]!=tho[i-1]:
        kq+='1'
    if tho[i]=='7':
        dem+=1
        if dem==4:
            kq+='2'
            dem=0

print(len(kq))
for i in kq:
    print(int(i))
        



    
    

