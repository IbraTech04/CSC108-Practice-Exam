def mystert(arr):
    n = len(arr)
    size = 1
    while size < n:
        for left in range(0, n - 1, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            scooby_doo(arr, left, mid, right)
        size *= 2


def scooby_doo(arr: list[int], a: int, b: int, c: int):
    i = a
    j = b + 1

    while i <= b and j <= c:
        if arr[i] <= arr[j]:
            i += 1
        else:
            temp = arr[j]
            for k in range(j, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = temp

            i += 1
            b += 1
            j += 1

    while j <= c:
        arr[b + 1] = arr[j]
        j += 1
        b += 1

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
scooby_doo(my_list, 0, 2, 6)
print("Merged array:", my_list)


