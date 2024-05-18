
def check(arr):
    for i in range(1,4):
        if arr[i]!=arr[0]: return False

    return True


while True:
    arr=[int(x) for x in input().split()]
    if check(arr)==True:
        if arr[0]==0: break
    
    dem=0
    while(check(arr)==False):
        dem+=1
        tam=arr[0]
        arr[0]=abs(arr[0]-arr[1])
        arr[1]=abs(arr[1]-arr[2])
        arr[2]=abs(arr[2]-arr[3])
        arr[3]=abs(arr[3]-tam)
        
    print(dem)
   