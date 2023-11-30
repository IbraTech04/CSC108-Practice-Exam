

def is_happy(n: int) -> bool:
    for i in range(7):
        n = sum([int(x) ** 2 for x in str(n)])
    return n == 1

print(is_happy(19))
