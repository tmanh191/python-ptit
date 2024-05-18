ll='.!?'
a=[]
while True:
    try:
        s=input()
        s=s.lower()
        s=s.strip()
        x=''
        for i in s:
            if i in ll:
                x=x.strip()
                if len(x)>0:
                    x+=i
                    a.append(x)
                x=''
            else:
                x+=i
            
            # if i in delim:
            #     x = x.strip()
            #     if len(x) > 0:
            #         x += i
            #         a.append(x)
            #     x = ''
            # else:
            #     x += i
        
        x=x.strip()
        if len(x)>0:
            a.append(x)
    except Exception:
        break

for i in a:
    text=i.split()
    res=''
    for j in text:
        res+=j+' '
    res=res.strip()
    
    if res[-1] not in ll:
        res+="."
    res=res.capitalize()
    print(res)
    