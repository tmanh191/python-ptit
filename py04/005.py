import math
class P:
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def kc(self,k):
        a=self.x-k.x
        b=self.y-k.y
        return math.sqrt(a**2+b**2)
class tri:
    def __init__(self,p1,p2,p3) :
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def cnt(self):
        a=self.p1.kc(self.p2)
        b=self.p2.kc(self.p3)
        c=self.p3.kc(self.p1)
        if(max(a, b, c) * 2 >= a + b + c) : print('INVALID')
        else : print('{:.3f}'.format(a + b + c))
            
            
            
a=[]
t=int(input())
for _ in range(t):
    a+= [float(x) for x in input().split()]
i=0
for index in range(t):
    trii= tri( P(a[i],a[i+1]),P(a[i+2],a[i+3]),P(a[i+4],a[i+5]) ) 
    trii.cnt()
    i+=6
