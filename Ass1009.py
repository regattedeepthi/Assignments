class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def get_info(self):
        return "Brand: " + self.brand + ", Year: " + str(self.year)

class Car(Vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors
    
    def get_info(self):
        return "Brand: " + self.brand + ", Year: " + str(self.year) + ", Number of doors: " + str(self.number_of_doors)
class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
    
    def get_info(self):
        sidecar = "Yes" if self.has_sidecar else "No"
        return "Brand: " + self.brand + ", Year: " + str(self.year) + ", Has sidecar: " + sidecar


c = Car("Hyundai", 2021, 4)
mc = Motorcycle("Harley Davidson", 2020, True)

print(c.get_info())  
print(mc.get_info()) 


"""2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method."""
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof"
class Cat(Animal):
    def make_sound(self):
        return "Meow"
class Cow(Animal):
    def make_sound(self):
        return "Moo"
def play_sound(animal):
    print(animal.make_sound())
dog=Dog()
cat=Cat()
cow=Cow()
play_sound(dog)
play_sound(cat)
play_sound(cow)

"""Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage."""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        return "name: "+self.name + ", Salary: $" + str(self.salary) 
    def get_salary(self):
        return self.salary
    def increase_salary(self,percent):
        self.salary+=self.salary*percent/100
class Manager(Employee):
     def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
     def get_details(self):
        return  super().get_details() + ", Department: " + self.department
class Developer(Employee):
    def __init__(self,name, salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def get_details(self):
        return super().get_details()+ ", programming language: " + self.programming_language

emp=Employee("Shiva",30000)
mngr=Manager("Ram",35000,"Team leader")
dev=Developer("Rani",30000,"Python")
print(emp.get_details())
print(mngr.get_details())
print(dev.get_details())
emp.increase_salary(10)
mngr.increase_salary(10)
dev.increase_salary(10)
print("Details after increasing salary")
print(emp.get_details())
print(mngr.get_details())
print(dev.get_details())

"""5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method. Demonstrate polymorphism by passing different types of media to this function."""

from abc import ABC,abstractmethod
class Media(ABC):
    @abstractmethod
    def play(self):
        pass
class Audio(Media):
    def __init__(self,file_name):
        self.mp3filename=file_name
    def play(self):
        print("playing audio file: ",self.mp3filename)
class Video(Media):
    def __init__(self,mp4file_name):
        self.mp4filename=mp4file_name
    def play(self):
        print("playing video file: ",self.mp4filename)

class LiveStream(Media):
    def __init__(self,livestream) -> None:
        self.livestream=livestream
    def play(self):
        print("Playing livestream: ",self.livestream)
def start_media(media):
    media.play()
audio=Audio("Background music")
video=Video("Cartoon film")
liveStream=LiveStream("Dandiya live show")
start_media(audio)
start_media(video)
start_media(liveStream)

