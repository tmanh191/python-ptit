n=int(input())
a=[]
for i in range(n):
    he=input().strip()
    if he not in a:

        a.append(he)

print(len(a))