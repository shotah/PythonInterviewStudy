# https://emre.me/algorithms/greedy-algorithms/

# Minimum Coin Change Problem

denominations = [1, 5, 10, 25, 50, 100]
# 100kr is ₺1


def return_change(change, denominations):
    to_give_back = [0] * len(denominations)

    # starting with the largest coin, goes through denominations list
    # and also keeps track of the counter, pos.
    for pos, coin in enumerate(reversed(denominations)):
        # while we can still use coin, use it until we can't
        while coin <= change:
            change = change - coin
            to_give_back[pos] += 1
    return to_give_back


print(return_change(267, denominations))
# returns [2, 1, 0, 1, 1, 2]
# 2x ₺1 (100 kr), 1x 50kr, 0x 25kr, 1x 10kr, 1x 5kr, 2x 1kr = 267kr = ₺2.67
