def element_access(Tuple_data):
    first_element = Tuple_data[0]
    last_element = Tuple_data[1]
    return first_element, last_element

input_tuple = eval(input("input tuple:"))
first, last = element_access(input_tuple)

print("first element:",first)
print("last element: ", last) 