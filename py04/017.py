def time(gio):
    return gio[0]*60-6*60+gio[1]
class ts:
    def __init__(self,ten,address, gio):
        self.ten=ten
        self.address=address
        tam=[str(x)for x in address.split()]
        tam+=[str(x) for x in ten.split()]
        a=''
        for x in tam:
            a+=x[0].upper()
        self.ma=a
        self.tt=time(gio)
        self.vt=round(120/(time(gio)/60))

    def info(self):
        print(self.ma,self.ten,self.address,self.vt, 'Km/h')

t=int(input())
a=[]
for _ in range(t):
    name=input().strip()
    ad=input().strip()
    ngu=[int(x) for x in input().split(':')]
    a.append(ts(name,ad,ngu))

a=sorted(a,key=lambda x: x.tt)

for x in a:
    x.info()

        
