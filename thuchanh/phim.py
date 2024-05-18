def time(ngay):
    n,t,y=[int(x) for x in ngay.split("/")]
    return y*365+t*30+n


class phim:
    def __init__(self,ma,theloai,ngay,ten,tap) :
        self.ma="P{:03d}".format(ma)
        self.theloai=theloai
        self.ngay=ngay
        self.ten=ten
        self.tap=tap
        self.sosanh=time(ngay)

    def info(self):
        print(self.ma,self.theloai,self.ngay,self.ten,self.tap)


n,m=[int(x)for x in input().split()]
a={}
for i in range(n):
    tl=input()
    a['TL{:03d}'.format(i+1)]=tl

arr=[]
for i in range(m):
    tl=input()
    theloai=a[tl]
    ns=input()
    ten=input()
    tap=input()
    arr.append(phim(i+1,theloai,ns,ten,tap))

arr=sorted(arr,key=lambda x: x.sosanh)

for i in arr:
    i.info()


cách đọc file trong python với file có dạng 
AAA BAABA HDHDH ACBSD SRGTDH DDDDS
DUAHD AAA AD DA HDHDH AAA AAA AAA AAA
DDDAS HDHDH HDH AAA AAA AAA AAA AAA
AAA AAA AAA
DHKFKH DHDHDD HDHDHD DDDHHH HHHDDD
TDTD

và tao muốn đọc từng từ của nó



