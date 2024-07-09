

class h:
    def __init__(self,ma,ten,gio,sx):
        self.ma=ma+" "
        self.ten=ten
        self.gio=gio
        self.sx=sx

    def f(self):
        print(self.ma,self.ten,self.gio)




def phut(s):
    return (int(s[0])*60+int(s[1]))

def chuyen(a):
    phut=a%60
    gio=int(a/60)
    return "{} gio {} phut".format(gio,phut)

a=[]
t=int(input())
for i in range(t):
    ma=input()
    ten=input()
    vao=input().split(":")
    ra=input().split(":")

    chenhphut=phut(ra)-phut(vao)
 
    s=chuyen(chenhphut)
    a.append(h(ma,ten,s,chenhphut))

a=sorted(a,key=lambda x: -x.sx)

for i in a:
    i.f()


