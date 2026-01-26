# a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping through a string

# loop through the letters in the word "banana":
for x in "banana":
    print(x)

# The break statement can be used to stop a for loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

print("----------------------------------------------------------------------------------")
# The continue statement can be used to stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("----------------------------------------------------------------------------------")
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)

print("----------------------------------------------------------------------------------")
# range() defuaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:

for x in range(2, 6):
    print(x)

print("----------------------------------------------------------------------------------")
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter:

for x in range(2, 30, 3):
    print(x)

print("----------------------------------------------------------------------------------")
# else in for loop

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished second!")

print("----------------------------------------------------------------------------------")
# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print("----------------------------------------------------------------------------------")
# The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.

for x in [0, 1, 2]:
    pass