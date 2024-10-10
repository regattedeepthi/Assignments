#super()= this function is used to give access to a methods of a parent class
#returns temporary object of a parent class when used
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)  
    def area(self):
        return self.length*self.width     
class Cube(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length,width)
        self.height=height
    def volume(self):
        return self.length*self.width*self.height
square=Square(5,5)
cube=Cube(5,5,5)      
print(square.area())
print(cube.volume())

#Python follows Method Resolution Order (MRO), which ensures that the base class (A) is initialized only once, avoiding the "diamond problem."
#The diamond problem refers to an issue that arises in multiple inheritance when a class inherits from two classes that both inherit from a common base class.
class A:
    def __init__(self):
        print("A is a constructor")
class B(A):
    def __init__(self):
        print("B is a constructor")
        super().__init__()
class C(A):
    def __init__(self):
        print("C is a constructor")
        super().__init__()
class D(B,C):
    def __init__(self):
        print("D is a constructor")
        super().__init__()
d=D()
