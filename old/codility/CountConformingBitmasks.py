import re
from itertools import product
from typing import List, Set

def get_zeros_indexes(a: str) -> List[int]:
    """
    finds all the zeros in the binary and gets their index.
    """
    return [index.start() for index in re.finditer(pattern="0", string=a)]

def get_nums(a) -> Set[str]:
    """
    creates all possible permutations of binaries of flipping zeros to ones.
    """
    indexes_of_zero = get_zeros_indexes(a)
    result = set()
    products = list(product(["0", "1"], repeat=len(indexes_of_zero)))
    for prod_arr in products:
        str_a = list(a)
        for idx, num in enumerate(prod_arr):
            str_a[indexes_of_zero[idx]] = num
        result.add("".join(str_a))
    return result

def get_bins(a: int, b: int, c: int) -> List[str]:
    """
    Method to convert ints to bins of length 30
    """
    return ["{0:030b}".format(bin) for bin in [a, b, c]]

def solution(a: int, b: int, c: int) -> int:
    """
    calls convert and get products of binaries and returns the length of arrays
    """
    result = set()
    for bin in get_bins(a, b, c):
        result.add(bin)
        for k in get_nums(bin):
            result.add(k)
    return len(result)


a = (1073741727, 1073741631, 1073741679)
# a= (0,0,0)
print(solution(*a))
