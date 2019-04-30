letters = ['a', 'b', 'c', 'd', 'e', 'f']

# Adding Items
letters.append('q')
letters.insert(0, '-')

# removing Items which are already in the list
letters.pop()  # Removes last item in the list
letters.pop(2)  # Providing the index will remove the item from the list
letters.remove('e')  # Searches and removes the first occurence from the list
del letters[0:3]
print(letters)

letters = []
print(letters)
