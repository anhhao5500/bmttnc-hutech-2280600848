def divisible_by_5(binary):
    decimal = int(binary, 2)
    if decimal % 5 == 0:
        return True 
    else:
        return False

binary_number_string = input( "Enter string of binary numbers:")

binary_list = binary_number_string.split(',')
number_divisible_by_5 = [num for num in binary_list if divisible_by_5(num)]

if len(number_divisible_by_5) > 0:
    result = ','.join(number_divisible_by_5)
    print( "Numbers can divisible by 5: ", result )
else:
    print("there's no number can be divisible by 5")
    