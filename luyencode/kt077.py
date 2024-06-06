from datetime import datetime

class h:
    def __init__(self,ma,mamon,tenmon,ngay,ca) :
        self.ma="T{:03d}".format(ma)
        self.mamon=mamon
        self.tenmon=tenmon
        self.ngay=ngay
        self.ca=ca
        self.obj_date=datetime.strptime(ngay,"%d/%m/%Y %H:%M")

    def f(self):
        print(self.ma,self.mamon,self.tenmon,self.ngay,self.ca)




n,m=[int(x) for x in input().split()]
tl={}
a=[]
for i in range(n):
    ma=input()
    ten=input()
    tl[ma]=ten

for i in range(m):
    t=input().split()
    a.append(h(i+1,t[0],tl.get(t[0]),t[1]+" "+t[2],t[3]   ))

a=sorted(a,key=lambda x: x.obj_date)

for i in a:
    i.f()