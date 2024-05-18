import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distance(self, k):
        a=self.x-k.x
        b=self.y-k.y

        return math.sqrt( a*a+b*b)
class Triangle :
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def area(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(max(a, b, c) * 2 >= a + b + c) : print('INVALID')
        else :
            d = math.sqrt((a + b + c) * (a + b - c) * ( a + c - b) * (-a + b + c)) / 4
            print('{:.2f}'.format(d))
        

# class Triangle:
#     def __init__(self,p1,p2,p3):
#         self.p1=p1
#         self.p2=p2
#         self.p3=p3
    
#     def area(self):
#         a=self.p1.distance(self.p2)
#         b=self.p2.distance(self.p3)
#         c=self.p3.distance(self.p1)
#         if max(a,b,c)*2>= a+b+c: print("INVALID")
#         else:
#             S= math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))/4
#             print("{:.2f}".format(S))

a=[]
t=int(input())
for _ in range(t):
    a+=[float(x) for x in input().split()]
i=0
for _ in range(t):
    triangle=Triangle(Point(a[i],a[i+1]),Point(a[i+2],a[i+3]),Point(a[i+4],a[i+5]))
    triangle.area()
    i+=6