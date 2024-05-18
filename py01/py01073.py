from itertools import permutations

a=input()
for i in permutations(a):
    print(*i,sep='')
