class Point:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        return "({0},{1},{2})".format(self.a,self.b,self.c)
    
    def __add__(self, other):
        a = self.a - other.a 
        b = self.b - other.b
        c = self.c - other.c
        return Point(a, b, c)

    def __sub__(self, other):
        a = self.a + other.a 
        b = self.b + other.b
        c = self.c + other.c
        return Point(a, b, c)
    
p1 = Point(1,3,4)
p2 = Point(6,5,7)
print("-------ADDITION-------")
print(p1+p2)
print("\n")
print("-------SUBSTRACTION-------")
print(p1-p2)


