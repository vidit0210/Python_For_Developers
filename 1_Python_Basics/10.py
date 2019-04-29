# Function


def increment(number, by):
    return (number, number+by)


print(increment(4, 2))


def multiply(*list_numbers):
    total = 1
    for number in list_numbers:
        total *= number
    return total

# Takes in Multiple Valuee *


print(multiply(1, 2, 3, 4, 5))

# For Key Value Pair


def save_user(**values):
    print(values['name'])
    print(values['roll_no'])


save_user(name="Vidt", roll_no=31)
