def time(x,y):
    return y[0]*60+y[1]-x[0]*60-x[1]

a={}
n=int(input())
for i in range(n):
    name=input()
    x=[int(x) for x in input().split(":")]
    y=[int(x) for x in input().split(":")]
    lm=int(input())

    if name not in a:
        a[name]=(time(x,y),lm)
    else:
        a[name]=(a[name][0]+time(x,y), a[name][1]+lm)

p=1
for i in a:
    print("T{:02d}".format(p),i, "{:.2f}".format(a[i][1]*60/a[i][0]) )
    p+=1

# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35