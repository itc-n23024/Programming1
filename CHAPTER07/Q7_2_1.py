def list_del_nth(list_, index):
    try:
        del list_[index]
    except IndexError:
        print("Index Not Found")
    except:
        print("Unexpected Error")
    else:
        print("Successfully")


my_list = ["v", "w", "x", "y"]
list_del_nth(my_list, "5")
list_del_nth(my_list, 5)
list_del_nth(my_list, 0)

print(my_list)
