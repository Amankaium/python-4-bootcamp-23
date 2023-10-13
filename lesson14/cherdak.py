def unpack(lst, res=[]):
    for element in lst:
        if isinstance(element, list):
            unpack(element, res)
        else:
            res.append(element)
    return res

lst_1 = [5, 7, [9, 0], [3, [6, 2, 6], 5, [7, 2]], 62, [[[[[[[[[[[[[7, 32, 7, 2]]]]]]], 83]]]]]]]
result_1 = unpack(lst_1)
print(result_1)

# lst_2 = [6, 9, [5, 2]]
# result_2 = unpack(lst_2)
# print(result_2)