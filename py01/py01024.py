def check(a):
    dem=0
    for x in a:
        dem+=int(x)

    if( dem%10!=0): return False

    for i in range(1,len(a)):
        if abs(int(a[i])-int(a[i-1]))!=2: return False

    return True

t=int(input())
for _ in range(t):
    a=input()
    if(check(a)):
        print("YES")
    else:
        print("NO")