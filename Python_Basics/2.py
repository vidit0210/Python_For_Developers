# Strings


"""
escape sequences Code ...
\" used for Displaying Double Quotes
\n new Line
\\ print a Slash
"""
course = "Python Programming"

print(len(course))
# Len inlcudes white spaces in them
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:])


# -------
firstName = "Vidit"
lastName = "Shah"
full_name = "{} {}  age is {}".format(firstName, lastName, 20+3)
print(full_name)
