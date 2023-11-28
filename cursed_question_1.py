def cursed_funct_junior(i : int) -> int:
    lst = [0, 0, 1]
    for _ in range(i):
        lst.append(lst[-2])
        lst.append(lst[-2])
        lst.append(lst[-2] + lst[-1])
    return lst[-1]

print(cursed_funct_junior(4))