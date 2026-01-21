print("The 3 numeric types are int, float, and complex")

a = 5
b = 27.5
c = 5j 

print(type(a))
print(type(b))
print(type(c))

print("an int is any whole number postive or negative without a decimal")
print("A float is any number postive or negative with a decimal, can also be scientific numbers with " \
"an e to indicate the power of 10.")
print("A complex number is a number with a real and imaginary part")

x = 35e5
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))  

e = 3 + 5j
f = -7.25 + 0j
g = 0j

print(type(e))
print(type(f))  
print(type(g))

print("Type Conversion")
print("I can convert from one type to another with the int(), float(), and complex() methods")

x = 5
y = 2.8
z = 5j + 6

a = float(x) #convert from int to float
b = int(y)   #convert from float to int
c = complex(x) #convert from int to complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print(" Built in module called random, that can be used to generate random numbers.")

import random
print(random.randrange(1, 100))