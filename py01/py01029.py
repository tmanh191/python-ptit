import math
def check(a,b):
    if math.gcd(int(a),int(b))==1: return True
    else: return False


a=input().split()

n=int(a[0])
k=int(a[1])
dem=0
for i in range(10**(k-1),10**k-1):
    if(check(n,i)):
        print(i,end=' ')
        dem+=1
    if(dem==10): 
        print()
        dem=0
    