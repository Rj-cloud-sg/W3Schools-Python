# While loop can execute a set of statements as long as a condition is true.

# print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1  

# The break statement can be used to stop a while loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue statement can be used to stop the current iteration, and continue with the next:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else statement can be used with a while loop.

# print a message once the condition is no longer true:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")