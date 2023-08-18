def list_average(a):
    try:
        return sum(a)/len(a)
    except:
        print('list_lenrth:', len(a))
        return None

    print(list_average([9.9, 4.1, 8.4]))
    print(list_average([]))
