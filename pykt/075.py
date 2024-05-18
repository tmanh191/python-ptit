from datetime import datetime
class sv:
    def __init__(self,ngay,name,sdt) :
        x=name.split()
        self.ho = name.split()[-1]
        self.sx=datetime.strptime(ngay,'%d/%m/%Y')
        self.ngay=ngay
        self.name=name+':'
        self.sdt=sdt
    
    def info(self):
        print(self.name,self.sdt,self.ngay)

with open('E:\Code\Python\Code PTIT\pykt\SOTAY.txt','r') as f:
    text=f.read()

x=text.split("\n")

a=[]
i=0
ln=[]

while i<len(x):
    ht=x[i]
    if ht[:4]=='Ngay':
        ten=x[i+1]
        sdt=x[i+2]
        a.append(sv(ht[5:],ten,sdt))
        ln.append(ht)
        i+=3
    else:
        ten=x[i]
        sdt=x[i+1]
        ngay=ln[len(ln)-1][5:]
        a.append(sv(ngay,ten,sdt))
        i+=2

a=sorted(a,key=lambda x: (x.name,x.ho))
for i in a:
    i.info()





        


