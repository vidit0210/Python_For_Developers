from pprint import pprint
sentence = "This is a common Interview Question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_values = sorted(char_frequency.items(),
                       key=lambda kv: kv[1], reverse=True)

print(sorted_values[0])
