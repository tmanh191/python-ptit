n=int(input())
arr=sorted([float(x) for x in input().split()])
sum=0
dem=0
for i in range(1,n-1):
    if arr[i]>arr[0] and arr[i]<arr[n-1]:
        sum+=arr[i]
        dem+=1

print(round(sum/dem,2))
