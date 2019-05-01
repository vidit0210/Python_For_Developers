try:
    age = int(input("Enter Age"))
except ValueError:
    print("Enter Correct Value")
except NameError:
    print('Interger Expected')
