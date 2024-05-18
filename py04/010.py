class SV:
    def __init__(self,name,birtday,p1,p2,p3):
        self.name=name
        self.birtday=birtday
        self.p=p1+p2+p3

    def info(self):
        return self.name + " "+self.birtday +" "+ ('{:.1f}'.format(self.p))
    


name=input()
ns=input()
p1=float(input())
p2=float(input())
p3=float(input())

e=SV(name,ns,p1,p2,p3)
print(e.info())

