def hehe(a):
    a=int(a)
    sum=0
    if a==2: return 2
    
    i=2
    while(i<=a):
       
        while(a%i==0):
            a/=i
            sum+=i
        
        i+=1
    return sum

n=int(input())
sum=0
for _ in range(n):
    sum+=hehe(input())
print(sum)