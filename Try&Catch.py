try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)
    
except Exception as e:
    print(e) 

print("Thank You")

# raise 
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")
    
    
# try with else
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 

else:
    print("i am inside else!")
    


# try with finally
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 

finally:
    print("i am inside else!")
    
    
def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()

# file open check
try:
    with open("1.txt",'r') as f:
     print(f.read())
    
except Exception as e:
    print(e)
    
try:
    with open("2.txt",'r') as f:
     print(f.read())
    
except Exception as e:
    print(e)

try:
    with open("3.txt",'r') as f:
     print(f.read())
    
except Exception as e:
    print(e)

# divisible by zero 
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")