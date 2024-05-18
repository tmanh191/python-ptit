
class sp:
    def __init__(self,a,b) :
        self.a=a
        self.b=b

    def addd(self,x,y):
        e=x.a+y.a
        f=x.b+y.b
        self.a=e
        self.b=f

    def mul(self,x,y):
        e= x.a*y.a - x.b*y.b
        f= x.a*y.b + x.b*y.a
        self.a=e
        self.b=f

    def inf(self):
        if self.b<0:
            print("{} - {}i".format(self.a,-self.b),end='')
        else:
            print("{} + {}i".format(self.a,self.b),end='')

t=int(input())
for _ in range(t):
    a,b,c,d=[int(x) for x in input().split()]
    x=sp(a,b)
    y=sp(c,d)
    q=sp(0,0)
    k=sp(0,0)
    q.addd(x,y)
    k.mul(q,x)
    q.mul(q,q)
    

    k.inf()
    print(", ",end="")
    q.inf()
    print()
    
        