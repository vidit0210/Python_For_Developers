# List comprehension syntax

# [expression for item in items]

product_array = [
    ('Product1', 10),
    ('Product2', 8),
    ('Product3', 7),
]

map_price = list(map(lambda item: item[1], product_array))

# list Comprehension Method
compre_price = [item[1] for item in product_array]

print(map_price == compre_price)

# Filtering Method normally
filter_price = filter(lambda item: item[1] >= 8, product_array)

filter_compre = [item for item in product_array if item[1] >= 8]

print(filter_price == filter_compre)
age = 15
result = "Adult" if age >= 18 else "Minor"
print(result)
