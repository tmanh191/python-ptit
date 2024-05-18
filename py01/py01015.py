def check(a):
    for x in range(0,len(a)-1):
        if(a[x]>a[x+1]):
            return False
        
    return True


t=int(input())
for _ in range(t):
    a=input()
    arr= [int(char) for char in a]

    if check(arr):
        print("YES")
    else:
        print("NO")


