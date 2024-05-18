
class nv:
    def __init__(self,ma,ten,phong) :
        self.ma="C{:03d}".format(ma)
        self.ten=ten
        self.phong=phong
    
    def info(self):
        print(self.ma,self.ten,self.phong)
    
l=[]
n=int(input())
ll={}
for i in range(n):
    ma=input().strip()
    ten=input().strip()
    ll[i]=ma+" "+ten


def c(name):
    ma=int(name[-2:])
    return ma
n=int(input())
for i in range(n):
    ten=input()
    ma=int((input().strip())[-2:])-1
    l.append(nv(i+1,ten,ll[ma]))

l=sorted(l,key=lambda x: x.ten)
for i in l:
    i.info()
    