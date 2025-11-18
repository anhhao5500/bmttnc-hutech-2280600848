def reverse_list(lst):
    return lst[::-1]

input_list = input("please enter a list numeber you want to reverse, separated by comma: ")
number = list(map(int, input_list.split(',')))

list_reversed = reverse_list(number)
print(" list when reversed: ", list_reversed)