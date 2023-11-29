def cursed_list_1(lst1: list, lst2: list, call: callable) -> list:
    lst1 = [x for x in lst2[:1:-2]]
    lst2 = [x for x in lst1[1::2]]
    if lst1 == lst2:
        return lst1
    if len(lst1) > len(lst2):
        cursed_list_2 = lambda x, y: [x for x in y[:1:-2]]
    return call(lst1, lst2)
    
def cursed_list_2(lst1: list, lst2: list, call: callable) -> list:
    if len(lst1) >= (len(lst2)):
        cursed_list_1 = lambda x, y, z: [x for x in y[3::2]]
    return call(lst1, lst2, cursed_list_2)

print(cursed_list_2([1, 2, 3, 4, 5][::-1], [1, 2, 3, 4, 5][:2:-2], cursed_list_1))


# OLD:

"""
def cursed_list_1(a: list, b: list) -> list:
    if len(a) > len(b):
        return [x for x in a if x not in b]
    elif len(a) == len(b):
        return [x for x in b if x not in a]
    return []

def cursed_list_2(a: list, b: list) -> list:
    a = cursed_list_1 if a else [x for x in a if x in b]
    b = b if a else a
    return a(b, [x for x in a if x not in b])

print(cursed_list_2([1, 2, 3][::-1], [2, 3, 4][:2:-3]))

"""