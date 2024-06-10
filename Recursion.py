
# Factorial
def Factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*Factorial(n-1)

print(Factorial(5))

# Fibonacci 
def Fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    

print(Fibonacci(6))
