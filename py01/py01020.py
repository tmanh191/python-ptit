import math
def check(a):
   if a[len(a)-2:len(a)]=='86':
       return True
   
   return False
t=int(input())
for _ in range(t):
    a=input()

    if(check(a)):
        print("YES")
    else: print("NO")
    