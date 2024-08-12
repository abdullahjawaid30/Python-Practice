import math

class Programmer:
    company="Microsoft"
    def __init__(self,name,age,pin):
        self.name=name
        self.age=age
        self.pin=pin
        
        
Developer=Programmer("Robinson", 25, 334)
print(Developer.name,Developer.age,Developer.pin,Developer.company)

        
Developer=Programmer("David", 25, 334)
print(Developer.name,Developer.age,Developer.pin,Developer.company)



class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n * self.n

    def cube(self):
        return self.n * self.n * self.n

    def squareRoot(self):
        return math.sqrt(self.n)
    
    @staticmethod
    def hello():
        print("Hello There!")

calculation = Calculator(4)
calculation.hello()
print(f"The Square of {calculation.n} is {calculation.square()}")
print(f"The Cube of {calculation.n} is {calculation.cube()}")
print(f"The Square Root of {calculation.n} is {calculation.squareRoot()}") 



class Demo:
    a=0
    
Demo1=Demo()
print(Demo1.a)

Demo1.a=20
print(Demo1.a)


