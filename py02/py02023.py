import functools
def h(a):
    sum=0
    a=str(a)
    for i in a:
        sum+=int(i)

    return sum
def cmp(a, b) :
    if h(a) == h(b) :
        if a > b : return 1
        else : return -1
    elif h(a) > h(b) : return 1
    else : return -1
t = int(input())
for i in range(t) :
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = functools.cmp_to_key(cmp))
    for i in a : print(i, end = " ")
    print()