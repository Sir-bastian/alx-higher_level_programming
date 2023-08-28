#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        qoutient = a / b
    except ZeroDivisionError:
        qoutient = None
    finally:
        print("Inside result: {}".format(qoutient))
    return qoutient
