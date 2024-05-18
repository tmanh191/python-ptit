def nt(a):
    if a==2 or a==3 or a==5 or a==7 : return True
    else: return False

def check(a):
    if nt(len(a))==False: return False

    dem=0
    for x in a:
        if(nt(int(x)==True)): dem+=1
    
    if dem> len(a)-dem: return True
    else : return False

t=int(input())
for _ in range(t):
    if(check(input().strip())): print("YES")
    else: print("NO")



    