
class h:
    def __init__(self,ma,ten,t):
        self.ma="KH{:02d}".format(ma)
        self.ten=ten
        s=t
        if s <= 50:
            s *= 100
            s += s * 0.02
        elif s <= 100:
            s = 50 * 100 + (s - 50) * 150
            s += s * 0.03
        else:
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.t=round(s)

    def f(self):
        print(self.ma,self.ten,"{:.0f}".format(self.t))

a=[]
t=int(input())
for i in range(t):
    ten=input()
    d1=int(input())
    d2=int(input())

    a.append( h(i+1,ten,d2-d1  ))
a=sorted(a,key=lambda x: -x.t)
for i in a:
    i.f()