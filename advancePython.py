# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)
    
# type operator
from typing import List, Union, Tuple 

n : int = 5

name: str = "Harry"


def  sum(a: int, b: int) -> int:
    return a+b

# Match Case
def http_status(status): 
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"  


print(http_status(5007))

a=3

def myfun():
    global a
    a=40
    print(a)
    


myfun()
print(a)


l = [1, 2, 3, 4, 5, 6 ,7 , 8]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)
        

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)