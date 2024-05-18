t=int(input())
for _ in range(t):
    a=int(input())
    res='1 * '
    i=2
    while(a>1):
        dem=1
        while(a%i==0):
            a/=i
            
            if(a%i==0):
                dem+=1
            else:
                res+=str(i)+"^"+str(dem)+" * "
        
        
        i+=1

    print(res[0:len(res)-3])
    
    

