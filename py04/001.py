import math


class P:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance(self,a):
        f=math.sqrt( (a.x-self.x)**2+(a.y-self.y)**2  ) 
        return f
    
class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def check(self):
        ab= a.distance(b)
        bc= b.distance(c)
        ca= c.distance(a)
        maxx=max(ab,max(bc,ca))
       # print(ab,bc,ca,maxx,sep=' ')
        if ab+bc+ca>maxx*2: 
            print("{:.3f}".format(ab+bc+ca))
        else: print("INVALID")


t=int(input())
n=[]
for _ in range(t):
    ax,ay,bx,by,cx,cy=[int(x) for x in input().split()]
    a=P(ax,bx)
    b=P(bx,by)
    c=P(cx,cy)
    n.append(triangle(a,b,c))

for i in n:
    i.check()