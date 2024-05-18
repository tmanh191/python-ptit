a=[
    [10,12,14,20],
    [10,11,13,16],
    [9,10,12,14],
    [8,9,11,13]
]

class nv:
    def __init__(self,ma,ten,phong,luong) :
        self.ma=ma
        self.ten=ten
        self.phong=phong
        self.luong=luong
    
    def info(self):
        print(self.ma,self.ten,self.phong,"{}000".format(self.luong))
    
list_nv=[]
n=int(input())
list_phong={}
for i in range(n):
    text=input().split()
    phong=""
    for i in range(1,len(text)):
        phong+=text[i]+" "
    list_phong[text[0]]=phong[0:len(phong)-1]

n=int(input())
for i in range(n):
    ma=input()
    ten=input()
    luong=int(input())
    songay=int(input())
    x=0
    if ma[:1]=='A':
        x=0
    elif ma[:1]=='B':
        x=1
    elif ma[:1]=='C':
        x=2
    else:
        x=3
    y=int(ma[1:3])
    if y<4:
        y=0
    elif y<9:
        y=1
    elif y<16:
        y=2
    else:
        y=3
    
    list_nv.append(nv(ma,ten,list_phong[ma[3:5]],a[x][y]*luong*songay))


for i in list_nv:
    i.info()
    