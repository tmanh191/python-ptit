
import math

class d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def info(self):
        print("{:.0f} {:.0f}".format(self.x,self.y))
def check(a,b,c):
    if a<=0 or b<=0 or c<=0: 
        return False
    if max(a,b,c)*2<(a+b+c):
        return True  
    return False
def he(a,b,c):
    return 0.25*math.sqrt( (a + b + c) * (a + b - c) * (a - b + c) * (c + b - a) )
    # return 0.25*math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c))
class tam:
    def __init__(self,a,b,c):
        self.k1=float(math.sqrt( (a.x-b.x)**2 +(a.y-b.y)**2 ))
        self.k2=float(math.sqrt( (c.x-a.x)**2 +(c.y-a.y)**2 ))
        self.k3=float(math.sqrt( (b.x-c.x)**2 +(b.y-c.y)**2 ))
    
    def s(self):
        if check(self.k1,self.k2,self.k3):
            print("{:.2f}".format(he(self.k1,self.k2,self.k3)))
        else: print("INVALID")
    def info(self):
        print("{:.0f} {:.0f} {:.0f}".format(self.k1,self.k2,self.k3))

    

a=[]
t=int(input())
for _ in range(t):
    a+=[float(x) for x in input().split()]
i=0
for _ in range(t):
    triangle=tam(d(a[i],a[i+1]),d(a[i+2],a[i+3]),d(a[i+4],a[i+5]))
    triangle.s()
    i+=6
        
    
