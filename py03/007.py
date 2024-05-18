import re
input_text = """ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11."""
h='[.!?]'
line=re.split(h,input_text)
for i in line:
    if i!="":
        w=i.strip().split()
        s=""
        for j in w:
            s+=j.lower()+" "
    
        s=s[:1].upper()+s[1:]
        print(s)
   
