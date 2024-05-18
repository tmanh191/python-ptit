# a = {999: 2, 19: 1}

# # Sắp xếp từ điển theo giá trị giảm dần và khóa tăng dần nếu giá trị bằng nhau
# sorted_items = sorted(a.items(), key=lambda item: (-item[1], item[0]))

# # Lấy khóa của phần tử đầu tiên sau khi sắp xếp
# first_key = sorted_items[0][0]

# # In ra khóa của phần tử đầu tiên
# print("Khóa của phần tử đầu tiên:", first_key)



t=int(input())
for _ in range( t):
    n=int(input())
    a={}
    b=[]
    for i in range(n):
        x=int(input())
        if x not in a:
            a[x]=1
        else:
            lan=a[x]
            a[x]=lan+1
    
    c = sorted(a.items(), key=lambda x: (-x[1], x[0]))
    print(c[0][0])


# In ra khóa của phần tử đầu tiên
