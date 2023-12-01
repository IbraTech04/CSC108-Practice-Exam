import bisect


def num_eggs(egg_list: list[int], broken_egg_val: int) -> int:
    """
    Given a list of integers (in sorted order),
    returns the total number of broken eggs in the list.
    Precondition: egg_list is a list of integers.
    egg_list will only have 0s and 1s.
    The only broken eggs in egg_list will be in sequence.
    This method MUST be logn time complexity.
    """
    leftmost_egg = 0
    left, right = 0, len(egg_list) - 1
    while left < right:
        mid = (left+right)//2
        if egg_list[mid] < broken_egg_val: left = mid+1
        else: right = mid

    leftmost_egg = left
    left,right,mid = 0,len(egg_list)-1,0
    while left < right:
        mid = (left+right)//2
        if broken_egg_val < egg_list[mid]: right = mid
        else: left = mid+1
    
    rightmost_egg = right
    return rightmost_egg - leftmost_egg


print(num_eggs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0))
print(num_eggs([0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0))
print(num_eggs([0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 0))
print(num_eggs([1, 1, 1, 2, 2, 2, 2, 2, 2, 2], 2))
