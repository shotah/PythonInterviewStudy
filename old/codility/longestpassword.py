def validate_word(word: str) -> bool:
    """
    Checks word for alpha numeric
    Checks for odd nums
    Checks for even words
    """
    if not word.isalnum():
        return False
    len_numbers = len("".join([i for i in word if i.isdigit()]))
    if len_numbers % 2 == 0:
        return False
    len_alpha_word = len("".join([i for i in word if not i.isdigit()]))
    if len_alpha_word % 2 == 1:
        return False
    return True


def solution(s: str) -> int:
    """
    breaks up the strings and validates and returns the length of the longest string.
    """
    max_len = 0
    cur_len = 0
    for word in s.split():
        if validate_word(word):
            cur_len = len(word)
            max_len = max(max_len, cur_len)
    if not max_len:
        return -1
    return max_len


s = "test 5 a0A pass007 ?xy1"
print(solution(s))
