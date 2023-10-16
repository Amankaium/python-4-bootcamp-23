
def recursive_search(lst, target, index=0):
    if not lst:
        return -1

    if lst[0] == target:
        return index

    return recursive_search(lst[1:], target, index + 1)

lst = [1, 2, 3, 4, 5, 6, 7]
target = 5
result = recursive_search(lst, target)
print(result) 
