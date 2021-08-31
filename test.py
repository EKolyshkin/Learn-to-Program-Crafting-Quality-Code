def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    item = 0

    while item in range(0, k):
        initval = L[item]
        L[item] = L[len(L)-(item+1)]
        L[len(L)-(item+1)] = initval
        item += 1

    return L
