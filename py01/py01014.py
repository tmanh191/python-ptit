he=input()
string=he.split()

a=int(string[0])
k=int(string[1])
n=int(string[2])

check=False
b=k-a%k
for i in range(a+b,n+1,k):
    print(i-a,end=' ')
    check=True
        


if check==False:
    print(-1)
