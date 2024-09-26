#instance variable
class sample:
    def __init__(self):
        self.name="Ravi" #declaring inside the constructor using self
        self.id=1002
    def display(self):
        print(self.name)
        print(self.id)
        self.place="hyd" #declaring inside instance method using self
        print(self.place)

s=sample()
print(s.display()) # accessing outside class using object reference variable

#static variable
class demo:
    a=10 #declaring inside class diectly
    def __init__(self):
         self.b=20
         demo.c=30 #declaring inside constructor using class name
         print(demo.a)
    def show(self):
        demo.d=40 #declaring inside instance method using class name
        print(self.a+self.b+self.c+self.d)
dm=demo()
dm.show()

#Todays Assignment

#1.Create a class Person that has instance variables name, age, and gender. Add methods to:
#Initialize these variables.
#Update the age.
#Display the person's information.
 #Exercise:
 #> Create multiple instances of the Person class.
 #> Change the age of one person and display the updated information.
class Person:
    def __init__(self,name,age,gender):
        self.name= name 
        self.age= age
        self.gender=gender
  
    def display(self):
        print("Name: " + self.name + ", Age: " + str(self.age) + ", Gender: " + self.gender)
p1=Person("Rani",25,"Female")
p2=Person("Shiva",26,"Male")
p3=Person("Vishnu",22,"Male")
p4=Person("Sita",23,"Female")
p1.display()
p2.display()
p3.display()
p4.display()       
#updating the age of Person p4 
p4.age=18
print("updated_information: ")
p1.display()
p2.display()
p3.display()
p4.display()

#2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
 # Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  #Exercise:
   #>Create multiple employee instances.
   #>Print the total number of employees after adding each new employee.
   #>Check whether changing the total_employees in one instance affects the others.

class Company:
    Total_employees=0
    def __init__(self):
        self.employees={}
    def employee_info(self,name,department):
         self.employees[name] = department 
         
         Company.Total_employees+=1 #accessing static variable inside insatance method using class name
         print("employee name: ",name, "Dept: ",department )

emp=Company()
emp.employee_info("Ravi","Developer")  
emp.employee_info("Suresh","Tester")
emp.employee_info("Mahesh","Software Executive") 
emp.employee_info("Sangeetha","Developer") 
print("Total Employees: ",Company.Total_employees)  #Here Total employees is static variable we have to access outside class using class name

#3.Create a class Rectangle that has instance variables length and width. 
 # Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
 # Exercise:
  #  >Create instances of the Rectangle class with different lengths and widths.
 #   >Calculate and print the area for each rectangle.

class Rectangle:
   def __init__(self,length,width):
       self.length=length
       self.width=width
   def area(self):
       return self.length*self.width
r1=Rectangle(150,12)
r2=Rectangle(120,30)
r3=Rectangle(55,10)
print(r1.area())
print(r2.area())
print(r3.area())

#4.Create a class Employee where:
 # Each employee has an instance variable salary.
 # There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
 # Write a method total_salary that calculates the total salary for an employee (including the bonus).
 # Exercise:
 #  >Create several employee instances with different salaries.
  # >Change the bonus amount (static variable) and see how it affects all employees.
  # >Calculate and print the total salary for each employe

class Employee:
    bonus=10000
    def __init__(self,salary):
        self.salary=salary
    def total_salary(self):
        print(self.salary+Employee.bonus)
emp1=Employee(30000)
emp2=Employee(4000)
emp3=Employee(35000)
emp1.total_salary()
emp2.total_salary()
emp3.total_salary()
Employee.bonus=15000 #bonus changing
print("Emplopyees salary after bonus changed")
emp1.total_salary()
emp2.total_salary()
emp3.total_salary()