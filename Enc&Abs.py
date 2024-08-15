class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"This is class attribute {cls.a}")
    
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


class Employee1:
    salary=234
    increment=20
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary *(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=((salary/self.salary)-1 )*100
    







e = Employee()
e.a = 45
print(e.a)  # prints 45


e.name="Johny Sins"
print(e.name)

e.show()


e1=Employee1()
e1.salaryAfterIncrement=280
print(e1.increment)
