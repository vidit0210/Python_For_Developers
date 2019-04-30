product_array = [
    ('Product1', 10),
    ('Product2', 8),
    ('Product3', 7),
]

product_array.sort(key=lambda item: item[1])
print(product_array)


# Mappinng only price from th products
product_array = [
    ('Product1', 10),
    ('Product2', 8),
    ('Product3', 7),
]
prices_array = []
for price in product_array:
    prices_array.append(price[1])

print(prices_array)

# using maps to clarify stuff
prices = map(lambda price: price[1], product_array)
print(prices)
prices = list(map(lambda price: price[1], product_array))
print(prices)

# Now using Filtetr Functions
filtered_prices = filter(lambda item: item[1] >= 8, product_array)
print(filtered_prices)
