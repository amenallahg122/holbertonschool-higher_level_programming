#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for x in range(x):
            print('{}'.format(my_list[x]), end="")
            idx += 1
    except IndexError:
        pass
    print()
    return idx
