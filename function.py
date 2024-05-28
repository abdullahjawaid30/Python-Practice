def calculateMean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(x,y):
    if x > y:
        print("First Number Is Greater Than",x)
    else:
        print("Second Number Is Greater Than",y)


def name(fname,mname="Khan",lname="Watson"):
    print("Hello",fname,mname,lname)


def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum + i

    print("Average is :", sum/len(numbers))
    
def newName(**name):
    print("Good Evening",name["fname"],name["mname"],name["lname"])


def averageReturn(*numbers):
    sum=0
    for i in numbers:
        sum=sum + i

    return sum/len(numbers)


c=100
d=4
calculateMean(c,d)
isGreater(c,d)
name("Smith",'Deo')
calculateMean(b=2,a=88)
average(2,3,5,7,6)
newName(fname="John",mname="Deo",lname="Watson")
newNumber=averageReturn(9,20,8)
print("The Average number Of :",newNumber)