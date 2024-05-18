
class GV:
    def __init__(self,ma,ten,hehe,tin,cm) :

        self.ma="GV{:02d}".format(ma)
        self.ten=ten
        if hehe[0]=='A':
            self.mon="TOAN"
        elif hehe[0]=='B':
            self.mon="LY"
        else:
            self.mon='HOA'
        
        if hehe[1]=='1':
            self.diem=tin*2+cm+2.0
        elif hehe[1]=='2':
            self.diem=tin*2+cm+1.5
        elif hehe[1]=='3':
            self.diem=tin*2+cm+1.0
        else:
            self.diem=tin*2+cm
        
        if self.diem< 18:
            self.tt="LOAI"
        else:
            self.tt="TRUNG TUYEN"

    def info(self):
        print(self.ma,self.ten,self.mon,"{:.1f}".format(self.diem),self.tt)

t=int(input())

a=[]
for i in range(t):
    
    name=input()
    tt=input()
    tin=float(input())
    cm=float(input())
    a.append(GV(i+1,name,tt,tin,cm))

a=sorted(a,key=lambda x: -x.diem)

for x in a:
    x.info()


        