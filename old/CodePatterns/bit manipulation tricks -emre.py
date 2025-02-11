# https://emre.me/computer-science/bit-manipulation-tricks/

def even_or_odd_checker(num: int) -> str:
    if (num & 1) == 0:
        return f"{num} is EVEN"
    else:
        return f"{num} is ODD"
      
      
def check_nth_bit(num, n: int) -> str:
    # test nth bit if its set to 1, else false if 0. "(1 << n)" <- is nth bit
    if num & (1 << n):
        return f"{num} = {bin(num)} (binary) and {n}th bit is set"
    else:
        return f"{num} = {bin(num)} (binary) and {n}th bit is NOT set"
      

# Set the n-th bit if it is not already set
def set_nth_bit(num, n: int) -> str:
    if num & (1 << n):
        return f"{num} (decimal) = {bin(num)} (binary) and {n}th bit is ALREADY set"
    else:
        set_nth_bit_result = num | (1 << n)
        return f"{n}th bit is set ({bin(num)} is changed to {bin(set_nth_bit_result)})"

# Unset n-th bit if it is not already unset  
def unset_nth_bit(num, n: int) -> str:
    if num & (1 << n):
        unset_nth_bit_result = num & ~(1 << n)
        return f"{n}th bit is unset ({bin(num)} is changed to {bin(unset_nth_bit_result)})"
    else:
        return f"{num} (decimal) = {bin(num)} (binary) and {n}th bit is ALREADY unset"

# Toggle the n-th bit  
def toggle_nth_bit(num, n: int) -> str:
    toggled_number = num ^ (1 << n)
    return f"{n}th bit of {bin(num)} toggled and the result is {bin(toggled_number)}"
  
# Turn off the rightmost 1-bit
def turn_off_rightmost_1bit(num: int) -> str:
    rightmost_1bit_turned_off = num & (num - 1)
    return f"Rightmost 1-bit in {bin(num)} is turned off and the result: {bin(rightmost_1bit_turned_off)}"

# Isolate the rightmost 1-bit
def isolate_rightmost_1bit(num: int) -> str:
    isolated_number = num & (-num)
    return f"Rightmost 1-bit in {bin(num)} is isolated and the result: {bin(isolated_number)}"

# Isolate the rightmost 0-bit
def isolate_rightmost_0bit(num: int) -> str:
    isolated_number = ~num & (num + 1)
    return f"Rightmost 0-bit in {bin(num)} is isolated and the result: {bin(isolated_number)}"

# Turn on the rightmost 0-bit
def turn_on_rightmost_0bit(num: int) -> str:
    rightmost_0bit_turned_on = num | (num + 1)
    return f"Rightmost 0-bit in {bin(num)} is turned on and the result: {bin(rightmost_0bit_turned_on)}"
