

def chuye(s):
    x=0
    for i in s:
        x+= ord(i)-ord('0')
    return str(x)

a=input()
dem=0
while(len(a)>1):
    dem+=1
    a=chuye(a)

print(dem)


