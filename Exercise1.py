a1=340;
a2=69;

b=a1+a2;
c=a1-a2;
d=a1*a2;
e=a1/a2;
f=a1//a2

print("The Sum Of two Number is", b);
print("The Subtraction Of two Number is", c);
print("The Multipilication Of two Number is", d);
print("The Division Of two Number is", e);
print("The Flot without point value Of two Number is", f);


# Typecasting in Python

# Explicit Type Casting
string1="15"
number1=7

string_Number=int(string1)
sum1=number1 +string_Number;
print("The Sum Of String And Number is", sum1);

# Imlicit Type Casting
number2=15
float1=3.4

print(type(number2))
print(type(float1))

sum2=number2+float1;

print("The Sum Of Number And Float is", sum2);
