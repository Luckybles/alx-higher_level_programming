#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    update_list = []
    for items in range(len(my_list)):
        if my_list[items] % 2 == 0:
            update_list.append(True)
        else:
            update_list.append(False)
    return update_list
