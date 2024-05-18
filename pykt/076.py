from datetime import datetime

class phim:
    def __init__(self,ma,theloai, ngay, phimso,sl) :
        self.ma='P{:03d}'.format(ma)
        self.theloai=theloai
        self.ngay=ngay
        self.phimso=phimso
        self.sl=sl
        self.date_obj=datetime.strptime(ngay,"%d/%m/%Y")
    def info(self):
        print(self.ma,self.theloai,self.ngay,self.phimso,self.sl)

n,m=[int(x) for x in input().split()]
a=[]
tl={}
for i in range(n):
    tl["TL{:03d}".format(i+1)]=input().strip()

for i in range(m):
    tloai=input().strip()
    ngay=input().strip()
    phimso=input().strip()
    sl=int(input())
    
    a.append(phim(i+1,tl[tloai],ngay,phimso,sl))

a=sorted(a,key= lambda x: (x.date_obj,x.phimso,-x.sl))
for i in a:
    i.info()