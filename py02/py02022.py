sang=[False]*100000
sang[0]=sang[1]=True

for i in range(2,1000):
    if sang[i]==False:
        for j in range(i*i,100000,i):
            sang[j]=True

n=int(input())
arr=[int(x) for x in input().split()]
m={}
for i in range(n):
    if sang[arr[i]]==False:
        if arr[i] not in m:
            print(arr[i]," ",arr.count(arr[i]))
            m[arr[i]]=1

