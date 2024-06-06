import re

h='!?.'
regex='[\w\s!?.,:]+'
s=[]
while True:
    try:
        t=input()
    except: break
    #thêm ~
    u=''
    for i in t:
        if i in h:
            u+=i+'~'
        else:
            u+=i
    s.append(u)
# print(s)
b=[]
for i in s:
    i=re.findall(regex,i)
    for u in i:
        b.append(u.strip())
c=[]
for i in b:
    i=i.capitalize().split()
    i=' '.join(i)
    if i[len(i)-1] not in h:
        i+="."
    else:
        if i[len(i)-2]==' ':
            i=i[:len(i)-2]+i[len(i)-1]
    
    c.append(i)

for i in c:
    print(i)