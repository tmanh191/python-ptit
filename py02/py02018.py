n=int(input())
arr=sorted([int(x) for x in input().split()])
check=False
for i in range(1,n):
    if arr[i]-i!=arr[0]:
        check=True
        print(arr[i-1]+1)
        break

if check==False: print(arr[n-1]+1)