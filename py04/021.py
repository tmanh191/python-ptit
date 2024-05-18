def timep(i,o):
    return o[0]*60+o[1]-i[0]*60-i[1]

class net:

    def __init__(self,ma,ten,vao,ra):
        self.ma=ma
        self.ten=ten
        self.phut=timep(vao,ra)
    
    def info(self):
        he="{} gio {} phut".format(int(self.phut/60),self.phut%60)
        print(self.ma,self.ten,he)



n=int(input())
a=[]
for i in range(n):
    ma=input()
    ten=input()
    vao=[int(x) for x in input().split(":")]
    ra=[int(x) for x in input().split(":")]
    a.append(net(ma,ten,vao,ra))

a=sorted(a,key=lambda x: (- x.phut))

for i in a:
    i.info()