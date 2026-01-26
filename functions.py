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

