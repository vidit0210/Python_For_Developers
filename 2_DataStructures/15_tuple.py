# tuples
point = (1, 2)
x, y = point
print(x)
if 1 in point:
    print('Yes')

# Tuples are immuatable if can't be edited after creating them
a = 10
b = 11
temp = a
a = b
b = temp
print(a)
print(b)
a, b = b, a
