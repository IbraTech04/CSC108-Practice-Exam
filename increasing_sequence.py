def is_ibra_list(lst: list[int]):
    start, end, longest = 0, 0, 0
    for i in range(len(lst)):
        if lst[i] > lst[end]:
            end += 1
        else:
            start = i
            end = i
        longest = max(longest, end - start + 1)
    return longest

