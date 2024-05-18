class sv:
    def __init__(self,ma,ten,lop,diemdanh,stt):
        self.stt=stt
        self.ma=ma
        self.ten=ten
        self.lop=lop
        diem=10
        for i in diemdanh:
            if i=='v': diem-=2
            else:
                if i=='m': diem-=1
        self.diem=diem
        
    def info(self):
        if self.diem<=0: 
            print(self.ma,self.ten,self.lop,"0 KDDK")
        else:
            print(self.ma,self.ten,self.lop,self.diem)
    


a={}
list_sv=[]
n=int(input())
for i in range(n):
    ma=input()
    ten=input()
    lop=input()
    a[ma]=(ten,lop,i)

for i in range(n):
    ma,d=[str(x) for x in input().split()]
    list_sv.append(sv(ma,a[ma][0],a[ma][1],d,a[ma][2]))

list_sv=sorted(list_sv,key=lambda x: x.stt)
for i in list_sv:
    i.info()


     
     