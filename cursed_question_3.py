def cursed_list_1(a: list, b: list) -> list:
    if a == [] or b == []:
        return lambda x, y: x if x else y
    if len(a) > len(b):
        return [x for x in a if x not in b]
    elif len(a) == len(b):
        return [x for x in b if x not in a]
    return []

def cursed_list_2(a: list, b: list) -> list:
    a = cursed_list_1 if a else [x for x in a if x in b]
    return a(b, [x for x in b if x not in [x for x in a if x in b]])

print(cursed_list_2([1, 2, 3][::-1], [2, 3, 4][:2:-3]))