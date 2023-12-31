#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            qoutient = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            qoutient = 0
        except ZeroDivisionError:
            print("division by 0")
            qoutient = 0
        except IndexError:
            print("out of range")
            qoutient = 0
        finally:
            new_list.append(qoutient)
    return new_list
