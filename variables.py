print("variables in python do not need a type to be set")

x = 5
x = "RJ"
print(x)

print("I can set a type by casting", end=" using str(), int(), float(), etc "); 

x = str(5)
y = int(8)
z = float(10) 
print(x, y, z)

print("I can also get the typ of any variable using the type() function ");

h = "100"
print(type(h))
print(type(y))

print("Variable Names")
print("Acceptable variable names", end=" myDog, MyCar, my_money, test_Case_1, MyMomsDocs.")
myDog = "Fido"
MyCar = "Toyota"
my_money = 1000
test_Case_1 = True
MyMomsDocs = ["doc1", "doc2", "doc3"]

print(myDog)
print(MyCar)
print(my_money)
print(test_Case_1)
print(MyMomsDocs)

print("Multiple Variables")
print("In python I can assign values to mutliple variables in one line.")

a, b, c = "green", "1 million", "Freedom"
print(a)
print(b)
print(c)

print("I can also assign the same value to mutliple variables")
x = y = z = "Rich"
print(x)
print(y)
print(z)

print("If i have a list, Python allows me to axtract variables the values into variables.", end=" Called unpacking. \n")
fruits = ["apple", "banana", "cherry"]
f1, f2, f3 = fruits
print(f1)
print(f2)   
print(f3)

print("Output Variables")
x = "RJ"
y = 5
z = 10

print("My name is", x)
print(x, y)
print(y + z)
print(y * 10)
