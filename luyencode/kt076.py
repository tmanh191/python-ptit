from datetime import datetime

class phim:
    def __init__(self,ma,tl,ngay,phimso,sl) :
        self.ma="P{:03d}".format(ma)
        self.tl=tl
        self.ngay=ngay
        self.phimso=phimso
        self.sl=sl
        self.date_obj= datetime.strptime(ngay,"%d/%m/%Y")

    def f(self):
        print(self.ma,self.tl,self.ngay,self.phimso,self.sl)



n,m=[int(x) for x in input().split()]
tl={}
a=[]
for i in range(n):
    tl["TL{:03d}".format(i+1)]=input().strip()




for i in range(m):
    tloai=input().strip()
    ngay=input().strip()
    phimso=input().strip()
    sl=int(input())
    
    a.append(phim(i+1,tl[tloai],ngay,phimso,sl))

a=sorted(a,key= lambda x: x.date_obj)
for i in a:
    i.f()