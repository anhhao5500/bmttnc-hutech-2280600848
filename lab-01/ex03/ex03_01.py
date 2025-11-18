def even_sum(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num 
    return total
input_list  = input("Input a list of numbers separated by comma: ")
numbers  = list(map(int, input_list.split(',')))

result = even_sum(numbers)
print("The sum of all the even numbers in the list: ", result)