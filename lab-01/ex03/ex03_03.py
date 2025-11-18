def create_tuple_form_list(lst):
    return tuple(lst)
input_list = input("please enter a list of number you want, separated by comma: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = create_tuple_form_list(numbers)
print("list : ", numbers)
print("tuple from list: ", my_tuple)