import math
class ps:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def toigian(self):
        a=self.x
        b=self.y
        n=math.gcd(a,b)
        a/=n
        b/=n
        print(int(a),int(b),sep='/')

    def tong(self,b):
        self.x=self.x*b.y+self.y*b.x
        self.y=self.y*b.y
        self.toigian()

    
        

x,y,p,q=[int(x) for x in input().split()]
a=ps(x,y)
b=ps(p,q)
a.tong(b)
