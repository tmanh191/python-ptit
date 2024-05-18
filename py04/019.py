def hihi(a):
    if a>10: return float(a/10)
    else: return float(a)
class hier:
    def __init__(self,ma,ten,lt,th):
        self.ma=ma
        self.ten=ten
        self.diem=float((hihi(lt)+hihi(th))/2)

        if self.diem<5:
            self.xh="TRUOT"
        elif self.diem<8:
            self.xh="CAN NHAC"
        elif self.diem<=9.5:
            self.xh="DAT"
        else:
            self.xh="XUAT SAC"
    
    def info(self):
        print(self.ma,self.ten,"{:.2f}".format(self.diem),self.xh)

n=int(input())
a=[]
for i in range(n):
    ten=input()
    ma = "TS0" + str(i+1)
    lt=float(input())
    th=float(input())
    a.append(hier(ma,ten,lt,th))

a=sorted(a,key=lambda x: (-x.diem))

for i in a:
    i.info()

    
