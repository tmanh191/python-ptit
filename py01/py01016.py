t=int(input())
for _ in range(t):
    a=input()
    for x in range(0,int(len(a)/2)):
        print(a[x*2]*int(a[x*2+1]),end='')
    print()