# Instead of many if-else statements, we can use match-case to select among multiple options.

from unittest import case


def run():
    day = 4
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
run()


def test():
    day = 4
    match day:
        case 6:
            print("Today is Saturday")
        case 7:
            print("Today is Sunday")
        case _:
            print("Looking forward to the Weekend")

test()

## Combine values

def combine():
    day = 4
    match day:
        case 1 | 2 | 3 | 4 | 5:
            print("Weekday")
        case 6 | 7:
            print("Weekend")
combine()

# can add if statements as an extra condition check

def iStatement():
    month = 5
    day = 4
    match day:
        case 1 | 2 | 3 | 4 | 5 if month == 5:
            print("It's May Weekday")
        case 6 | 7:
            print("It's Weekend")
        case _:
            print("It's not May Weekday")
iStatement()