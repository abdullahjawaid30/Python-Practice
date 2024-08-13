class Employee:
    company = "RT-Development"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coders:
    def __init__(self, position, experience):
        self.position=position
        self.experience=experience
    
    def showExperience(self):
        print(f"The coder has {self.experience} years of experience")
        
    def showPosition(self):
        print(f"The coder is a {self.position}")
        
        
        
class Programmer(Employee,Coders):
    company = "RT-Solutions"

    def __init__(self, name, salary, language, position, experience):
        Employee.__init__(self, name, salary, language)
        Coders.__init__(self, position, experience)

    def show_language(self):
        print(f"The programmer knows {self.language}")
        
        
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
          print("Bow Bow!")
            
        
        
        
        
        

programmer = Programmer("Abdullah", 34343, "Python","RPA Developer",6)
programmer.show()
programmer.show_language()
programmer.showPosition()
programmer.showExperience()

dogi=Dog()
dogi.bark()




