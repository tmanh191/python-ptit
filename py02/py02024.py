import functools
def c(h):
    h=str(h)
    tich=1
    for i in h:
        tich*=int(i)
    return tich

def cmp(a,b):
    a=int(a)
    b=int(b)
    if c(a)>c(b): return 1
    elif c(a)==c(b):
        if a>b: return 1
        else: return -1
    else: return -1
        
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    arr=sorted(arr,key=functools.cmp_to_key(cmp))
    for i in arr : print(i, end = " ")
    print()