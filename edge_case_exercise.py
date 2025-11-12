def move(my_list, direction=None):
    index_of_one = my_list.index(1)
    
    if direction == 'right' and not my_list[-1] == 1:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
    elif direction == 'left' and not my_list[0] == 1:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1
    return my_list
