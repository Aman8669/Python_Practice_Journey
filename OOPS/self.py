class Employee():
    language = 'Python'
    salary = 1200000

    def __init__(self): # dunder method which is called automatically
        print("I am creating an Object using dunder method")

    @staticmethod  #it does not need self 
    def greet():
        print("Good Morning")

    def getInfo(self):
        print(f"The language is '{self.language}' and salary is {self.salary}")

e1 = Employee()

e1.greet()
e1.getInfo()