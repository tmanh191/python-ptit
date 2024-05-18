
def tron(a,i):
    if a[i + 1] >= 5:
        a[i + 1] = 0
        a[i] += 1
    else:
        a[i + 1] = 0

t=int(input())
for _ in range(t):
    a=input().strip()
    arr=[int(char) for char in a]

    for i in range(len(a)-2,-1,-1):
        tron(arr,i)

    print("".join(map(str,arr)))


    
