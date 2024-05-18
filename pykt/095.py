
class hd:
    def __init__(self,ma,ten,ki,so) :
        self.ma="KH{:02d}".format(ma)
        self.ten=ten
        if ki=="A":
            self.dm=100
        elif ki=="B":
            self.dm=500
        else:
            self.dm=200

        if so<self.dm:
            self.tiendm= so*450
        else:
            self.tiendm=self.dm*450

        if so> self.dm:
            self.tienvuotdm=(so-self.dm)*1000
        else:
            self.tienvuotdm=0
        self.vat=round(self.tienvuotdm/20)

        self.tien=self.tiendm+self.tienvuotdm+self.vat

    def info(self):
        print(self.ma,self.ten,self.tiendm,self.tienvuotdm,self.vat,self.tien)

def chuanhoa(name):
    tus=name.split()
    tuschuan=[tu.capitalize() for tu in tus]
    tenchuan= ' '.join(tuschuan)
    return tenchuan

a=[]
t=int(input())
for i in range(t):
    ten=input()
    x=input().split()
    a.append(hd(i+1,chuanhoa(ten),x[0],  int(x[2])-int(x[1])  ))

a=sorted(a,key=lambda x: -x.tien)
for i in a:
    i.info()


        