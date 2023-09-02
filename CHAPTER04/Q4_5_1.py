functions = [sum, max, min]
number_list = [i for i in range(1, 11)]
for func in functions:
    print("Function: {}, Result: {}".format(func.__name__, func(number_list)))
