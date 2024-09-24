#creating class and objects 
class Myclass():
    def Myfunc(self):
        pass
    def display(self):
        print("python")
m=Myclass()
m.Myfunc()
m.display()



class func:
     def __init__(self,a,b):
        self.a=a
        self.b=b
     def display(self):
         return self.a+self.b
     def mul(self):
             return self.a*self.b
p=func(10,20)
print(p.a)
print(p.b)
print(p.display())
I= func(12,12)
print(I.a)
print(I.b)
print(I.display())
print(I.mul())


class products:
     def __init__(self,name,price):
          self.name=name
          self.price=price
     def display(self):  
          return "Product Name: " + self.name + ", Price: " + str(self.price)  
x=products("Books",200)
print(x.display())        
s=products("Bags",200)
print(s.display())