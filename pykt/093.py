import math

class sv:
    def __init__(self,ma,ten,diem) :
        self.ma="SV{:02d}".format(ma)
        self.ten=ten
        self.diem=diem
        self.xh=1

    def getD(self):
        return self.diem
    def getXh(self):
        return self.xh
    def setXh(self,xh):
        self.xh=xh

    def info(self):
        d=math.ceil(self.diem/8*100)/100
        print(self.ma,self.ten,"{:.2f}".format(d),self.xh)

def chuanhoa(name):
    words=name.split()  
    a='kdsj'
    a.capitalize
    hehe=[word.capitalize() for word in words]
    you= ' '.join(hehe)
    return you

a=[]
n=int(input())
for i in range(n):
    ten=chuanhoa(input().strip())
    d1=int(input())
    d2=int(input())
    d3=int(input())
    a.append(sv(i+1,ten,(d1+d2)*3+d3*2))

a=sorted(a,key=lambda x: (-x.diem,x.ma))

for i in range(1,len(a)):
    if a[i].getD()==a[i-1].getD():
        a[i].setXh(a[i-1].getXh())
    else:
        a[i].setXh(i+1)


for i in a:
    i.info()  