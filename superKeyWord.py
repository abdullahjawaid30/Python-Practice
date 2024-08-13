class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)  
        self.age = age

    def bark(self):
        print(f"{self.name} is barking.")
        
        
class twoDVector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"In TwoDVector ({self.x}, {self.y})")

class threeDVector(twoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"In ThreeDVector ({self.x}, {self.y}, {self.z})") 
        

dog = Dog("Buddy", 3)
dog.eat()  
dog.bark()  

a=twoDVector(1,2)
a.show()
b=threeDVector(5,6,7)
b.show()