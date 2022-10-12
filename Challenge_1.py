from re import X


class Point:
    final_square = 0
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
            
    def sqSum(self):
        self.x = self.x * self.x
        self.y = self.y * self.y
        self.z = self.z * self.z
        return self.x+self.y+self.z


x=int(input("Enter the first element: "))
y=int(input("Enter the second element: "))
z=int(input("Enter the third element: "))

point_obj = Point(x,y,z)
final_square = point_obj.sqSum()
print(final_square)
