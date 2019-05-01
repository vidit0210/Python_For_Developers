def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    values = [item for item in in_list if item > 0]
    sorted_item = values.sort()
    return sorted_item[0]


in_list = [4, -6, 7, 2, -4, 10]
values = [item for item in in_list if item > 0]
values.sort()
print(values)
