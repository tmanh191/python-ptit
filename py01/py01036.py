t=int(input())
for _ in range(t):
    a=int(input())
    dem=0.0
    if(a%2==0):
        
        for x in range(2,a+1,2):
            dem+=float(1/x)

        print(f"{dem:.6f}")
    else:
        
        for x in range(1,a+1,2):
            dem+=float(1/x)
        print(f"{dem:.6f}")
