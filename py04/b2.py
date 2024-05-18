from itertools import permutations

al = "AEIOUY"

n = 6  # Số phần tử trong tập
k = 2  # Số phần tử trong mỗi hoán vị

# Tạo các hoán vị chập k của n
perms = list(permutations(range(1, n+1), k))
i=0
for perm in perms:
    i+=1
    print("KH",al[perm[0]-1],al[perm[1]-1],"U",sep='')

print('total', i)

# KHIEU
# KHOAU
# KHUYU
