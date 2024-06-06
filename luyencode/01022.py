n=int(input().strip())
n=str(n)
sum=0
lan=0
while len(n)>1 :
    sum=0
    lan+=1
    for i in n:
        sum+=ord(i)-ord('0')
    n=str(sum)
if(lan==0): lan=1

print(lan)


