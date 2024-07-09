import re

regex='[\w\s:,]+'
u=[]
while True:
    try:
        t=input()
    except: break
    u.append(t)
b=[]
for i in u:
    i=re.findall(regex,i.lower())
    for u in i:
        u=u.strip().split()
        u=' '.join(u)
        b.append(u)

for i in b:
    print(i.capitalize())