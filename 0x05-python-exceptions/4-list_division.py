#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Args:
        my_list_1 (_type_): _description_
        my_list_2 (_type_): _description_
        list_length (_type_): _description_
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            result = 0
            print("out of range")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(result)
    return new_list
