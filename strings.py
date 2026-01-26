print("You can use quotes inside a string as long as they dont match the outer quotes.")

print("His name is 'RJ'")

print("Because strings are arrays in Python, square " \
"brackets can be used to access elements of the string.")

a = "Hello, World!"
print(a[7]) 

print("You can loop through the characters in a string with a for loop.")

for x in "banana":
  print(x)

  

print("Use len() to get the length of a string.") 
a = "Hello, World!"
print(len(a))

print("Check if certain character or phrase is present in a string with the in keyword.")
txt = "The best things in life are free!"
print("free" in txt)

txt1 = "What are you going to do without food?"
print("cash" in txt1)

print("Use in if statements")

txt2 = "Money is not everything"
if "Money" in txt2:
  print("Yes, it is everything") # to check if not just add "not" in front of "in"

print("====================================================================================")
print("Return a range of characters by using the slice syntax.")

b = "Rj is number 5, and he plays football"
print(b[5:12])
print(b[:5]) #by leaving out the start index, it starts at the first character
print(b[2:]) #gets the charcters from index 2 to the end
print(b[-5:-1]) #negative indexing starts from the end of the string

print("====================================================================================")
print("Combine two strings with +")

z = "Rj is"
y = " number 5"
print(z + y)

twoStrings = z + y
print(twoStrings)

print("====================================================================================")
print("to combine a string with a variable we use an f string, can add math operators")

age = 20

ageTxt = f"RJ is {age} years old"
print(ageTxt)



