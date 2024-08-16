from functools import reduce
# Map Example 
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter Example
def even(n):
    if (n%2 == 0):
        return True 
    return False

onlyEven= filter(even, l)
print(list(onlyEven))


def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a  = [1,2,34234,53,6234235,64343, 65,754,45,55]

f = list(filter(divisible5, a))
print(f)



# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))


l  = [111, 2, 65, 5553, 635, 65, 74, 45,55]


def greater(a, b):
    if (a>b):
        return a 
    return b

print(reduce(greater, l))


