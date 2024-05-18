from datetime import datetime

class KH:
    def __init__(self,ma,ten,sophong,songay,phatsinh) :
        self.ma=ma
        self.ten=ten.title()
        self.sophong=sophong
        self.songay=songay
        if sophong[0]=='1':
            self.thanhtien=songay *25+phatsinh
        elif sophong[0]=='2':
            self.thanhtien=songay *34+phatsinh
        elif sophong[0]=='3':
            self.thanhtien=songay *50 +phatsinh
        else:
            self.thanhtien=songay *80+phatsinh
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.sophong} {self.thanhtien}"
    
def chuan(date_str):
    return datetime.strptime(date_str,'%d/%m/%Y')

def chenh(den,di):
    return (chuan(di)-chuan(den)).days+1

def main():
    
    n=int(input())
    danh_sach=[]
    dem=0
    for _ in range(n):
        dem+=1
        ten=input().strip()
        sophong=input().strip()
        den=input().strip()
        di=input().strip()
        
        phatsinh=int(input().strip())
        danh_sach.append(KH("KH{:02d}".format(dem), ten, sophong, chenh(den, di), phatsinh))

    danh_sach.sort(key=lambda x:x.thanhtien, reverse=True)

    for kh in danh_sach:
        print(kh)

if __name__=="__main__":
    main()