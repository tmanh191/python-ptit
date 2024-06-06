import numpy as np
import re

t=int(input())
for _ in range(t):
    n,m=[int(x) for x in input().split()]
    a=[]
    for i in range(n):
        row=[int(x) for x in input().split()]
        a.append(row)
    b=[]
    for i in range(m):
        x=[]
        for j in range(n):
            x.append(a[j][i])
        b.append(x)
    
    for i in range(n):
        for j in range(n):
            s=0
            for z in range(m):
                s+=a[i][z] * b[z][j]
            
            print(s,end=' ')
        print()