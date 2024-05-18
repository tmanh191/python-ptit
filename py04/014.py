from decimal import ROUND_HALF_UP,Decimal

id=1
class SV:
    msv='HS'
    d=0
    xh=''
    def __init__(self,ten,diem) :
        global id
        self.msv+='{:02d}'.format(id)
        id+=1
        self.ten=ten
        x=(diem[0]+diem[1])*2
        for i in  range(2,10):
            x+=diem[i]
        x/=12
        if x<5: self.xh="YEU"
        elif x<7: self.xh="TB"
        elif x<8: self.xh="KHA"
        elif x<9: self.xh="GIOI"
        else: self.xh="XUAT SAC"
        self.dtb=x.quantize(Decimal('0.1'),ROUND_HALF_UP)

    def output(self):
        print(self.msv,self.ten,self.dtb,self.xh)

n=int(input())
a=[]
for i in range(n):
    b=input()
    c=[Decimal(x) for x in input().split()]
    a.append(SV(b,c))

a=sorted(a,key=lambda x: (-x.dtb,x.msv))
for i in a:
    i.output()

# 5
# Tran Van An
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
# Tran Trong Manh
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8