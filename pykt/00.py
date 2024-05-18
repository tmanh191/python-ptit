a=input().lower().split()
b=input().lower().split()

list1=[]
list2=[]
for i in a:
    if i not in list1:
        list1.append(i)
    if i in b and i not in list2:
        list2.append(i)
for i in b:
    if i not in list1:
        list1.append(i)
    if i in a and i not in list2:
        list2.append(i)


list1=sorted(list1)
list2=sorted(list2)
for i in list1:
    print(i,end=' ')
print()
for i in list2:
    print(i,end=' ')
