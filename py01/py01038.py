
t=int(input())
for _ in range(t):
    n=input()

    dem=0
    check=False
    while True:
        dem+=1
        if dem>1000: break
    
        if(int(n)%7==0):
            check=True
            break 

        n=str(int(n)+int(n[::-1]))

    if(check==False): print(-1)
    else: print(n)
    