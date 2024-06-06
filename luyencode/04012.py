
class h:
    def __init__(self,i,ma,ten):
        self.i=i
        self.ma=ma
        self.ten=ten
        self.d=0
        
    def setD(self,d):
        self.d=d

    def getM(self):
        return self.ma
    def f(self):
        if self.d==0:
            print(self.ma,self.ten,self.d,"KDDK")
        else:
            print(self.ma,self.ten,self.d)




tl={}
a=[]
t=int(input())
for i in range(t):
    ma=input()
    ten=input()+" "+input()
    a.append(h(i,ma,ten))

for i in range(t):
    ma,u=[str(s) for s in input().split()]
    d=10
    for i in u:
        if i=='v':
            d-=2
        if i=='m':
            d-=1 
        
    if d<0:
        d=0
    
    for i in a:
        if i.getM()==ma:
            i.setD(d)
    
    
a=sorted(a,key=lambda x: x.i)

for i in a:
    i.f()