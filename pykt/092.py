import math
class ts:
    def __init__(self,ma,ten,diem,dantoc,khuvuc) :
        self.ma="TS{:02d}".format(ma)
        self.ten=ten
        uutien=0.0
        if khuvuc==1:  uutien+=1.5
        elif khuvuc==2:  uutien+=1.0
        else:  uutien=0

        if dantoc!="Kinh":  uutien+=1.5
        self.diem=round((diem+uutien)*10)/10
        if self.diem<20.5: 
            self.tt='Truot'
        else:
            self.tt="Do"

    def info(self):
        print(self.ma,self.ten,"{:.1f}".format(self.diem),self.tt)

def chuanhoa(name):
    # Tách chuỗi thành các từ riêng biệt, loại bỏ các khoảng trắng thừa
    list_word = name.strip().split()

    # Chuẩn hóa từng từ trong danh sách từ
    standard_words = [word.capitalize() for word in list_word]

    # Kết hợp các từ đã chuẩn hóa thành một chuỗi mới
    standard_name = " ".join(standard_words)
    
    return standard_name


n=int(input())
a=[]
for i in range(n):
    name=chuanhoa(input())
    diem=float(input())
    dt=input()
    kv=int(input())
    a.append(ts(i+1,name,diem,dt,kv))

a=sorted(a,key=lambda x : (-x.diem,x.ma))
for i in a:
    i.info()
