import math

class ps:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def tong(self,a,b):
        xx=b.x*a.y+b.y*a.x
        yy=b.y*a.y

        u=math.gcd(xx,yy)
        self.x=xx/u
        self.y=yy/u

    def info(self):
        print("{:.0f}/{:.0f}".format(self.x,self.y))

a=input().split()

n=ps(int(a[0]),int(a[1]))
q=ps(int(a[2]),int(a[3]))
# n.info()
# q.info()
c=ps(0,1)
c.tong(n,q)
c.info()


