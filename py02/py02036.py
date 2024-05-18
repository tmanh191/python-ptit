import math
t=int(input())
arr= sorted([int(x) for x in input().split()])

for i in range(t-1):
    for j in range(i+1,t):
        if math.gcd(arr[j],arr[i])==1: print(arr[i]," ",arr[j])