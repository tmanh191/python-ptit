
class rectangle:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
       
        self.color=color[:1].upper()+color[1:].lower()

    def check(self):
        if self.x<=0 or self.y<=0: return 0
        else: return 1


    def ra(self):
        if self.check()==1:
           s=self.x*self.y
           V=self.x*2+self.y*2
           cl=self.color
           print(V,s,cl,sep=" ")
        else: print("INVALID")

def ra(a):
    s=a.x*a.y
    cv=a.x*2+a.y*2
    color=a.color
    return cv+" "+ s+" "+color

n=input().split()
a=rectangle(int(n[0]),int(n[1]),str(n[2]))
a.ra()
    
