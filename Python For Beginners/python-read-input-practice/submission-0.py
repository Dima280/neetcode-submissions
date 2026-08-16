def add_two_numbers() -> int:
    num = input()
    list_of_strings = num.split(',')
    list_of_int = []

    for string in list_of_strings:
        list_of_int.append(int(string))
    return list_of_int[0] + list_of_int[1]    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
