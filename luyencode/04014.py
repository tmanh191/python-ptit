
from decimal import ROUND_HALF_UP,Decimal



class h:
    def __init__(self,ma,ten,lm):
        self.ma="HS{:02d}".format(ma)
        self.ten=ten
        self.lm=Decimal(lm).quantize(Decimal('0.1'),ROUND_HALF_UP)
        if lm<5:
            self.xh="YEU"
        elif lm<7:
            self.xh="TB"
        elif lm<8:
            self.xh="KHA"
        elif lm<9:
            self.xh="GIOI"
        else: 
            self.xh="XUAT SAC"

        
    def ff(self):
        print(self.ma,self.ten,"{:.1f}".format(self.lm),self.xh)
def t(a):
    a=int(a)
    if a%10<5:
        return a-5
    else: 
        return a-a%10+10
    

def ttt(a):
    a=int(a*100)
    if a%10<5: 
        return a-a%10
    else:
        return a-a%10+10
a=[]
t=int(input())
for p in range(t):
    ten=input()
    d1=[float(x) for x in input().split()]
    tong=0.0
    for i in range(len(d1)):
        tong+=(d1[0]+d1[1])*2
        for i in range(2,len(d1)):
            tong+=d1[i]

    tong/=120
    # tong=ttt(tong)/100
    a.append(h(p+1,ten,tong))

a=sorted(a,key=lambda x: (-x.lm,x.ma))

for i in a:
    i.ff()
