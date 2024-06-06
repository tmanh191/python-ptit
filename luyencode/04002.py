def check(x,y):
    if x<=0 or y <=0 : return False

    return True


a=input().split()
x=int(a[0])
y=int(a[1])
c=a[2]
if check(x,y):
    print((x+y)*2,x*y,c.capitalize())
else:
    print("INVALID")