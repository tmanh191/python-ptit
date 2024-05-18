from datetime import datetime

class lich:
    def __init__(self,ma,mamon,tenmon,date_str,nhom):
        self.ma="T{:03d}".format(ma)
        self.mamon=mamon
        self.tenmon=tenmon
        self.date_str=date_str
        self.nhom=nhom
        self.date_obj=datetime.strptime(date_str,"%d/%m/%Y %H:%M")

    def info(self):
        print(self.ma,self.mamon,self.tenmon,self.date_str,self.nhom)

a=[]
ds={}

n,m=[int(x) for x in input().split()]
for i in range(n):
    ma=input().strip()
    ten=input()
    ds[ma]=ten


for i in range(m):
    t=input().split()
    mamon=t[0]
    tenmon=ds[t[0]]
    date_str=t[1]+" "+t[2]

    nhom=t[3]
    a.append(lich(i+1, mamon,tenmon,date_str,nhom ))

a=sorted(a,key=lambda x: (x.date_obj))

for i in a:
    i.info()