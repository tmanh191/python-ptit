
class p:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    


    def nhan(self,x,):
        aa=x.a*self.a-x.b*self.b
        bb=x.a*self.b+x.b*self.a
        self.a=aa
        self.b=bb
        
    def info(self):
        if self.b<0:
            print("{} - {}i".format(self.a,-self.b),end='')
        else:
            print("{} + {}i".format(self.a,self.b),end='')


t=int(input())
for _ in range(t):
    a=[int(x) for x in input().split()]
    A=p(a[0],a[1])
    B=p(a[2],a[3])

    ton=p(a[0]+a[2],a[1]+a[3])
    ton.nhan(A)
    ton.info()
    print(", ",end="")
    ton=p(a[0]+a[2],a[1]+a[3])
    ton.nhan(ton)
    ton.info()
    print()
