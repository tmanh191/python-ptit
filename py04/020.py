
class HD:
    def __init__(self,ma, ten, sl, tien, chiet):
        self.ma=ma
        self.ten=ten
        self.sl=sl
        self.tien=tien
        self.chiet=chiet
        self.tt=sl*tien-chiet

    def info(self):
        print(self.ma,self.ten,self.sl,self.tien,self.chiet,self.tt)

t=int(input())
a=[]
for _ in range(t):
    a.append(HD(input(),input(),int(input()),int(input()),int(input())))

a=sorted(a,key=lambda x: -x.tt)

for x in a:
    x.info()