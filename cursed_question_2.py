def cursed_funct_1(a: callable, b: callable, c: int, d:int) -> int:
    if c > d:
        increment = lambda x: 2*x
        return a(c//2) + b(d//2)
    else:
        increment = lambda x: 4*x
        return a(c//2) - b(d//2)

def increment(x: int) -> int:
    return x + 1

def decrement(x: int) -> int:
    return x - 1

def cursed_funct_2(a: callable, b: callable, c: int, d: int):
    a = cursed_funct_1 if a else increment
    b = b if a else a
    return a(b, decrement, c if a else c//2, d)


print(cursed_funct_2(increment, decrement, 7, 10))