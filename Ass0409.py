"""1. Single Inheritance
Problem Statement: Create a base class Animal with an attribute name and a method speak(). Then, create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".

Tasks:
Define a base class Animal with an __init__ method that takes name as a parameter.
Define a method speak() in Animal that prints "Animal sound".
Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
Create an instance of Dog and call the speak() method."""
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal sound")
        
class Dog(Animal):
    def speak(self):
       print("Bark")

d=Dog("shizo")
d.speak()          

"""2. Multiple Inheritance

1.Problem Statement: Create a class Teacher with an attribute subject. Then, create a class Researcher with an attribute field. Finally, create a class TeachingResearcher that inherits from both Teacher and Researcher, and has an additional method to display both attributes.

Tasks:
Define a Teacher class with an __init__ method to initialize subject.
Define a Researcher class with an __init__ method to initialize field.
Define a TeachingResearcher class that inherits from both Teacher and Researcher, and has an __init__ method to initialize both subject and field. Add a method to display both.
Create an object of TeachingResearcher and display its attributes."""

class Teacher:
    def __init__(self,subject):
        self.subject=subject
class Researcher :
    def __init__(self,field):
        self.field=field
class TeachingReasearcher(Teacher,Researcher):
    def __init__(self,subject,field):
        Teacher.__init__(self,subject)
        Researcher.__init__(self,field)
    def display(self):
        print(self.subject)
        print(self.field)
input_subject=input("Enter the subject name ")  
input_field=input("Enter field name ")      
TR=TeachingReasearcher(input_subject,input_field)  
TR.display()      

"""2.Problem Statement: Create two base classes: Bird and Flyable. Bird should have an attribute species, and Flyable should have a method fly(). Then, create a derived class Eagle that inherits from both Bird and Flyable.

Tasks:
Define a class Bird with an attribute species.
Define a class Flyable with a method fly() that prints "Flying".
Create a class Eagle that inherits from both Bird and Flyable, and has a method to display species and flying capability.
Create an instance of Eagle and call its methods."""

class Bird:
    def __init__(self,species) :
        self.species=species
class Flyable:
    def fly(self):
        print("Flying")   
class Eagle(Bird,Flyable):
    def __init__(self, species):
        Bird.__init__(self,species)
    def display(self):
        print(self.species)
        self.fly()
e=Eagle("Cassins Hawk Eagle")
e.display()

"""3. Multilevel Inheritance
Problem Statement: Create a class hierarchy where Person is the base class, Employee is derived from Person, and Manager is derived from Employee. Each class should add an additional attribute, and a method to display all attributes from the hierarchy.

Tasks:
Define a base class Person with attributes name and age.
Define a derived class Employee with an additional attribute salary.
Define another derived class Manager that inherits from Employee and adds an attribute department.
Implement methods to display the information in each class.
Create an instance of Manager and display its information."""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_info(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,name,age,salary):
        Person.__init__(self,name,age)      
        self.salary=salary
    def employee_info(self):
        self.person_info()
        print(self.salary)


class Manager(Employee):
    def __init__(self,name,age,salary,department):
        Employee.__init__(self,name,age,salary)
        self.department=department
    def Manager_info(self):
        self.employee_info()
        print(self.department)
manager=Manager("Ravi",30,50000,"Software Executive")
manager.Manager_info()

"""2.Problem Statement: Create a base class Vehicle with attributes brand and model. Then, create two derived classes Car and Bike, both inheriting from Vehicle, and adding their own attributes and methods.

Tasks:
Define a base class Vehicle with attributes brand and model.
Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
Create another derived class Bike that inherits from Vehicle and adds an attribute type.
Implement methods to display the details of the vehicles.
Create instances of both Car and Bike and display their information."""

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def  Vehicle_display(self):
        print(self.brand)
        print(self.model)
class Car(Vehicle):
    def __init__(self,brand,model,num_doors):
        Vehicle.__init__(self,brand,model)
        self.num_doors=num_doors
    def Car_display(self):
        self.Vehicle_display()
        print(self.num_doors)
class  Bike(Vehicle):
    def __init__(self,brand,model,type):
        Vehicle.__init__(self,brand,model)
        self.type=type
    def Bike_display(self):
        self.Vehicle_display()
        print(self.type)
c=Car("Hyundai","Verna",4)
B=Bike("Royal Enfield","Classic 350","Halcyon")
c.Car_display()
B.Bike_display()

"""5. Hybrid Inheritance
Problem Statement: Create a class structure to represent hybrid inheritance:

Device: Base class with name attribute.
Phone: Derived from Device with an additional phone_number attribute.
Tablet: Derived from Device with an additional screen_size attribute.
Smartphone: Derived from both Phone and Tablet with an additional attribute os.

Tasks:
Define a base class Device with an attribute name.
Define a class Phone that inherits from Device and adds an attribute phone_number.
Define a class Tablet that inherits from Device and adds an attribute screen_size.
Define a class Smartphone that inherits from both Phone and Tablet, adding an attribute os.
Implement methods to display all attributes of the Smartphone.
Create an instance of Smartphone and display its information."""

class Device:
    def __init__(self,name):
        self.name=name
    def display_device(self):
        print(self.name)
class Phone(Device):
    def __init__(self,name,phone_number):
        Device.__init__(self,name)
        self.phone_number=phone_number
    def display_phone(self):
        self.display_device()
        print(self.phone_number)
class Tablet(Device):
    def __init__(self,name,screen_size) :
        Device.__init__(self,name)
        self.screen_size=screen_size
    def display_tablet(self):
        self.display_device()  
        print(self.screen_size)       
class Smart_Phone(Phone,Tablet):
    def __init__(self,name,phone_number,screen_size,os):
        Phone.__init__(self,name,phone_number)
        Tablet.__init__(self,name,screen_size)
        self.os=os
    def display_smart_phone(self):
        self.display_phone()
        print(self.screen_size,"inches")
        print(self.os)
sp=Smart_Phone("Vivo V30",988812326,6.5,"Android")
sp.display_smart_phone()     


"""6.Basic Inheritance
Problem Statement: Create a class Person with attributes: name and age. Create another class Student that inherits from Person and has an additional attribute grade. Define methods in both classes to display the attributes.

Tasks:
Define a Person class with an __init__ method to initialize name and age.
Define a Student class that inherits from Person, with an additional attribute grade.
Define a display_info method in both Person and Student classes to print all attributes.
Create objects for both Person and Student and display their information."""

class Person:
    def __init__(self,name,age): 
        self.name=name
        self.age=age
    def display_person_info(self):
        print(self.name)
        print(self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        Person.__init__(self,name,age)
        self.grade=grade
    def Student_display_info(self):
        self.display_person_info()
        print(self.grade)
p=Person("Shiva",30)
p.display_person_info()
s=Student("Vikas",28,"A")
s.Student_display_info()
