import math
def check(a,b,c):
    if math.gcd(a,b)!=1 or math.gcd(b,c)!=1 or math.gcd(c,a)!=1: return False

    return True

a,b=[int(x)for x in input().split()]

for i in range(a,b+1):
    for j in range(i+1,b+1):
        for k in range(j+1,b+1):
            if check(i,j,k): 
                print("({}, {}, {})".format(i,j,k))