

class h:
    def __init__(self,ma,ten,lm,lan):
        self.ma="{:02d}".format(ma)
        self.ten=ten
        self.lm=lm
        self.lan=lan
    
    def set(self, a):
        self.lm=a
    
def hh(p1,p2):
    return ((p2[1]-p1[1])+(p2[0]-p1[0])*60) 

a={}
b={}
t=int(input())
for i in range(t):
    ten=input()
    phut=[int(x) for x in input().split(":")]
    phut2=[int(x) for x in input().split(":")]
    lm=int(input())
    # if ten=="Dong Anh":
    #     print(ten,hh(phut,phut2,lm),lm)

    if ten not in a:
        a[ten]=hh(phut,phut2)
        b[ten]=lm
    else:
        a[ten]=a.get(ten)+hh(phut,phut2)
        b[ten]=b.get(ten)+lm

# for i in a:
#     print(i,a.get(i),b.get(i))

lan=0
for i in a:
    lan+=1
    
    print("T{:02d} {} {:.2f}".format(lan,i,b.get(i)/a.get(i)*60))
