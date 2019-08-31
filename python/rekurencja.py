hard_list = [1, 2, 3, [[[[[[4, 5]]]]]], [[]], 6, [7], [[8, [9]]]]


def recurence(lst):
    for i in lst:
        if isinstance(i ,list):
            recurence(i)
        else:
            print(i)


recurence(hard_list)