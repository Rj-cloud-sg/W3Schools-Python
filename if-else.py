# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b 

a = 100
b = 200
 
if b > a:
    print("you won")
else:
    print("you lost")

number = 1

if number > 0:
    print("number is postitve")
else:
    print("the number is negative")

age = 21

if age >= 21:
    print("You are an adult")
    print("You can vote")
    print("You have full legal writes")
else:
    print("You are underage")

print("=========================================================")
# boolean values can be used in if statements

is_raining = True

if is_raining:
    print("Take an umbrella")

print("-----------------------------------------------------------------------")

# elif keyword is Pythins way if saying "if the previous conditions were not true, then try this condition"

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

score = 75

if score >=90:
    print("Grade A")
elif score >=80:
    print("Grade B")
elif score >=70:
    print("Grade C")
elif score >=60:
    print("Grade D")

age = 25

if age < 13:
    print("You are a child")
elif age < 15:
    print("You are in your teens")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age < 75:
    print("You are a senior adult")

day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

print("-----------------------------------------------------------------------------------")
# else statement catches anything that isn't caught before

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("b and a are equal")
else:
    print("a is greater than b")

score = 45
opponent_score = 50

if score > opponent_score:
    print("You win")
else:
    print("You lost")

number = 9
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

temperature = 22

if temperature> 30:
    print("It's hot outside")
elif temperature > 20:
    print("it's warm outside")
elif temperature > 10:
    print("it's cold outside")
else:
    print("It's freezing outside") 

# else statement acts as a fallback, making it useful for error handling

username = "RJ"

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty.")