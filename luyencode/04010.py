import datetime 
def chuan(ns):
    return "{:02d}/{:02d}/{}".format(ns[0],ns[1],ns[2])

ten=input()
ns=chuan([int(x)for x in input().split("/")])
d1=float(input())
d2=float(input())
d3=float(input())

print(ten,ns,"{:.1f}".format(d1+d2+d3))
