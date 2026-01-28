# a function is defined by the def keyword followed by the function name and parentheses ()

def my_function():
    print("Hello from a function")

my_function()  # calling the function to execute its code

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

print(fahrenheit_to_celsius(100))  # Example usage
print(fahrenheit_to_celsius(32))   # Example usage
print(fahrenheit_to_celsius(212))  # Example usage

def first_greeting():
    return "Hello, How are you?"

messege = first_greeting()
print(messege)

print("-------- Function Arguments -----------------------------------------------")

# info can be passed into functions as arguments, inside the parentheses.

def firstFunction(fname):
    print(fname + " Spencer")

firstFunction("RJ")
firstFunction("Brandy")
firstFunction("Jeremiah")
firstFunction("Alecia")

# A parameter is the variable lisrted inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
print("-----------------------------------------------------------------")
def nameFunction(name):
    print("Hello " + name)

nameFunction("RJ")

# If your function expects a number of arguments, it must recieve that same amount.

def fullName(firstName, lastName):
    print("Your full name is " + firstName + " " + lastName)

fullName("Ronnie", "Spencer")

# You can assign default values for parameters. If the function is called without an argument, the default value is used.

def stateFunction(state = "Michigan"):
    print("You are from " + state)

stateFunction()

# You can send arguments with the key = value syntax.

def hometownFunction(state, city):
    print("You were born in " + city + ", " + state)

hometownFunction(city = "Hunstville", state = "Alabama")

print("-----------------------------------------------------------------")

# You can send any data type as an argument

myFruits = ["apple", "banana", "cherry"]

def fruitFunction(fruits):
    for x in fruits:
        print(x)

fruitFunction(myFruits)

# Sending a dictionary as an argument

def personFunction(person):
    print("Name: " + person["name"])
    print("Age: " + person["age"])

myPerson = {"name": "RJ", "age": "20"}
personFunction(myPerson)

print("-----------------------------------------------------------------")
# Functions can return a value with the return statement.

def sumFunction(x, y):
    return x + y

result = sumFunction(10, 20)
print(result)

def multiplyFunction(a, b):
    return a * b

sumResult1 = multiplyFunction(10, 50)
print((multiplyFunction(sumResult1, 1)))

print("-----------------------------------------------------------------")
# functions can return any data type

# Function that returns a list

def fruitFunction():
    return ["apple", "banana", "cherry"]

fruits = fruitFunction()
print(fruits[0])
print(fruits[1])

def tupleFunction():
    return (100, 5000)

x, y = tupleFunction()
print("x:", x)
print("y:", y)

print("-----------------------------------------------------------------")
# Specify that a function can only have positional arguments with ,/ after an argument

def posArgFunction(name, /):
    print("Hello " + name)

posArgFunction("RJ")

# Keyword only by adding *, before argument

def keywordOnlyFunction(*, city):
    print("You live in " + city)

keywordOnlyFunction(city="Detroit")

# Combining / and *
# arguments before / are positional only
# arguments after * are keyword only

def combinedFunction(name, /, age, *, city):
    print("Hello " + name + ", you are " + str(age) + " and live in " + city)
    return "Hi I'm " + name, " I'm " + str(age) + " years old and live in " + city

result = combinedFunction("RJ", age=20, city="Lansing")


def numfunction(a, b, /, *, c, d):
  return a + b + c + d

result = numfunction(5, 10, c = 15, d = 20)
print(result)

print("-------------------------------------------------------------------------------")
