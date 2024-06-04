# https://emre.me/data-structures/lists/

# Time Complexities
# Operation	Worst Case
# copy()	O(n)
# append()	O(1)
# pop() - last	O(1)
# pop() - intermediate	O(n)
# insert()	O(n)
# Get Item	O(1)
# Set Item	O(1)
# Delete Item	O(n)
# Get Slice	O(k)
# Delete Slice	O(n)
# Set Slice	O(k + n)
# extend()	O(k)
# sort()	O(n log n)
# x in s	O(n)

# Creating a List

# empty list
list_empty = []

# list of integers
list_ints = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

# list of strings
list_strs = ['emre', 'dot', 'me']

# list of mixed data types
list_mixed = [1, 'emre.me', 5.73, True]

# nested list
list_nested = [['emre', 'dot', 'me'], [1], 5.73, True]

# Output: []
print(list_empty)

# Output: [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
print(list_ints)

# Output: ['emre', 'dot', 'me']
print(list_strs)

# Output: [1, 'emre.me', 5.73, True]
print(list_mixed)

# Output: [['emre', 'dot', 'me'], [1], 5.73, True]
print(list_nested)




# Accessing Elements of a List

# list
list_emre = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# Output: e
print(list_emre[0])

# Output: r
print(list_emre[-5])

# nested list
list_nested = ['emre', [1, 2, 3, [4]], False, 7.3, ['bolat']]

# Output: emre 
print(list_nested[0])

# Output: 1
print(list_nested[1][0])

# Output: 4
print(list_nested[1][3][0])

# Output: False
print(list_nested[2])

# Output: a 
print(list_nested[-1][0][3])


# Slicing Lists

# [-1]    # last item in the list
# [-2:]   # last two items in the list
# [:-2]   # everything except the last two items
# [::-1]    # all items in the list, reversed
# [1::-1]   # the first two items, reversed
# [:-3:-1]  # the last two items, reversed
# [-3::-1]  # everything except the last two items, reversed

list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# Output: ['e', 'm', 'r', 'e', '.', 'm', 'e']
print(list[:])

# Output: ['r', 'e', '.', 'm', 'e']
print(list[2:])

# Output: ['.']
print(list[4:5])

# Output: ['e', 'm', 'r', 'e']
print(list[:-3])

# Output: ['e', 'm', '.', 'e', 'r', 'm', 'e']
print(list[::-1])

# Output: ['.', 'e', 'r', 'm', 'e']
print(list[-3::-1])


# Add / Edit Elemets to a List

# create a list of numbers
list_nums = [0, 2, 3, 3, 3, 5]

# change 4th item
list_nums[4] = 4

# Output: [0, 2, 3, 3, 4, 5]
print(list_nums)

# change 2nd to 4th item
list_nums[1:3] = [1, 2]

# Output: [0, 1, 2, 3, 4, 5]
print(list_nums)


# append() and extend()

# create a list of numbers
list_nums = [0, 1, 2, 3, 4, 5]

# append "6" to the end of the list
list_nums.append(6)

# Output: [0, 1, 2, 3, 4, 5, 6]
print(list_nums)

# extend list with [7, 8, 9]
list_nums.extend([7, 8, 9])

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_nums)



# Concatenation and Repeating
# create list
list = ['e', 'm', 'r', 'e']

# Output: ['e', 'm', 'r', 'e', '.', 'm', 'e']
print(list + ['.'] + ['m', 'e'])

# Output: ['e', 'm', 'r', 'e', 'e', 'm', 'r', 'e']
print(list * 2)

# insert()
# We can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.

# create list
list = ['e', 'm', 'e']

# insert 'r' to 2nd position
list.insert(2, 'r')

# Output: ['e', 'm', 'r', 'e']
print(list)

# insert ['e', '.', 'm'] to 3rd position with using slices
list[3:3] = ['e', '.', 'm']

# Output: ['e', 'm', 'r', 'e', '.', 'm', 'e']
print(list)

# Delete / Remove Elements from a List
# We can delete one or more items, even an entire list with the del keyword.

# create a list
list_emre = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# delete the 4th element
del list_emre[4]

# Output: ['e', 'm', 'r', 'e', 'm', 'e']
print(list_emre)

# delete the slice from 4th to 6th
del list_emre[4:6]

# Output: ['e', 'm', 'r', 'e']
print(list_emre)

# delete entire list
del list_emre

# Output: 'list_emre' is not defined
print(list_emre)


# remove(), pop() and clear()
# We can use remove() method to remove the given item or pop() method to remove an item at the given index.

# The pop() method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).

# We can also use the clear() method to empty a list.

# create list
list_emre = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# removes the given item
list_emre.remove(".")

# Output: ['e', 'm', 'r', 'e', 'm', 'e']
print(list_emre)

# pops the element at 1st index
list_emre.pop(0)

# pops the element at 4th index
list_emre.pop(4)

# Output: ['e', 'm', 'r', 'e', 'e']
print(list_emre)

# pops the last element when index is not provided
list_emre.pop()

# Output: ['e', 'm', 'r', 'e']
print(list_emre)

# clears the list
list_emre.clear()

# Output: []
print(list_emre)



# index()
# Index method searches and finds given index and returns its position.

# create list
list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# search for "r"
index_of_r = list.index('r')

# Output: 2
print(index_of_r)
# if the same element is present more than once, only the first occurrence (smallest/first position) of the item returns.

# search for "m"
index_of_m = list.index('m')

# Output: 1
print(index_of_m)



# count()
# count() method counts how many times an item has occurred in a list.

# create list
list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# count the number of times "e" has occurred 
count_of_e = list.count('e')

# Output: 3
print(count_of_e)


# sort()
# sort() method sorts the elements of a list in a specific order (ascending or descending).

# Optional parameters:

# reverse: if true, sorted list is reversed (in descending order)
# key: key function for the sort comparison
# sort() method doesn’t return any value, it changes the original list.

# create list
list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# sort the list
list.sort()

# Output: ['.', 'e', 'e', 'e', 'm', 'm', 'r']
print(list)

# sort, reverse order
list.sort(reverse=True)

# Output: ['r', 'm', 'm', 'e', 'e', 'e', '.']
print(list)
# If you want the original list, use sorted().

# create list
list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# sorted
sorted_list = sorted(list)

# Output: ['.', 'e', 'e', 'e', 'm', 'm', 'r']
print(sorted_list)

# Reverse sorted
reverse_sorted_list = sorted(list, reverse=True)

# Output: ['r', 'm', 'm', 'e', 'e', 'e', '.']
print(reverse_sorted_list)
# It is also possible to sort a list with using your own function with the key= parameter.

# For example, let’s sort a list according to string length with using built-in len() method of Python.

# create list
list = ['emre', 'lists', 'sorting', 'python', 'is', 'fun']

# sort according to string length
list.sort(key=len)

# Output: ['is', 'fun', 'emre', 'lists', 'python', 'sorting']
print(list)
# Alternatively, you can use sorted(list, key=len).



# reverse()
# reverse() method does not take any arguments. It reverses the elements and updates the list.

# create list
list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# reversed
list.reverse()

# Output: ['e', 'm', '.', 'e', 'r', 'm', 'e']
print(list)
# Alternatively, you can use reversed(list) as well.

list = ['emre', '.', 'me']

for i in reversed(list):
    print(i)

# Output:

# me
# .
# emre





# copy()
# copy() method does not take any arguments and returns a list without modifying the original list.

list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

new_list = list.copy()
new_list = new_list[:-3]

# Output: ['e', 'm', 'r', 'e', '.', 'm', 'e']
print(list)

# Output: ['e', 'm', 'r', 'e']
print(new_list)


# Testing List Membership
# We can test if an item exists in a list or not, using the keyword in.

list = ['e', 'm', 'r', 'e', '.', 'm', 'e']

# Output: True
print('e' in list)

# Output: True
print('.' in list)

# Output: False
print('a' in list)


