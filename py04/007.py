def sum_row(matrix,a,b):
    sum=0
    for i in range(n):
        sum+=matrix[a][i]*matrix[b][i]

    
    return sum

t = int(input())
for _ in range(t):
    n,m=[int(x) for x in input().split()]
    matrix=[[0]*m for _ in range(n)]
    for i in range(n):
       matrix[i]=[int(x) for x in input().split()]

    for i in range(n):
        for j in range(m):
            print(sum_row(matrix,i,j),end=' ')
        print()

            


