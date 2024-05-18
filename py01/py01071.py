def check(a):
   if len(a)<3: return False

   if a[len(a)-3: len(a)].lower()!='.py': return False

   return True

t=int(input())
for _ in range(t):
    a=input().strip()
    if(check(a)): print("yes")
    else: print("no")
    