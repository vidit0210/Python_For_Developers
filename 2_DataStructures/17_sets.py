number_1 = [1, 2, 3, 3]
number_2 = [3, 4, 5, 6]

number_1 = set(number_1)
number_2 = set(number_2)

print(number_1 | number_2)
print(number_1 & number_2)

# To declare set you can use  = {} syntax
print(number_1 - number_2)
print(number_1 ^ number_2)  # Gives element which are not in both the sets

# can't Acess items using indexes in
