# https://emre.me/basic-types/strings/

# created a string variable called emre
emre = "emre.me"

# Get the character at position 0
# Output: e
print(emre[0])

# Get the substring character from position 4 to 5
# Output: .
print(emre[4:5])


# Concatenation and Repetition
# Strings are immutable in Python, they cannot be modified after being created. Using concatenation (+) and repetition (*) operators returns a new string.

# created some strings
str1 = "emre"
str2 = "."
str3 = "me"

# concatenation of strings
# Output: emre.me
print(str1 + str2 + str3)

# repetition operator
# Output: emreemreemre
print(str1 * 3)


# String Membership Test
# It is possible to test if a substring exists in a string or not, with using in and not in operators.

# created a string variable called emre
emre = "emre.me"

# Output: True
print("me" in emre)

# Output: False
print("xyz" in emre)

# Output: True
print("e.m.r.e" not in emre)


# Raw String
# Raw string operator (r) is useful for the cases where you need to print the actual meaning of escape character (\) such as C:\Program Files.

# Output: "emre.me"
print("\"emre.me\"")

# Output: \"emre.me\"
print(r"\"emre.me\"")


# .upper() and .lower()
# The functions .upper() and .lower() will return a string with all the letters from the original string converted to upper or lower case letters.

# created a new string
str1 = "Emre.Me"

# Output: emre.me
print(str1.lower())

# Output: EMRE.ME
print(str1.upper())


# .title, .swapcase() and .capitalize()
# .title() changes the first letter of each word to upper case and all other letters to lower case.

# .swapcase() method changes all upper case letters to lower case and vice versa.

# .capitalize() method works like .title() but it only changes the first letter of first word to upper case, and makes the rest lower case.

# create a new string
str1 = "EmRe Dot mE"

# Output: Emre Dot Me
print(str1.title())

# Output: eMrE dOT Me
print(str1.swapcase())

# Output: Emre dot me
print(str1.capitalize())



# Boolean Methods
# These string methods evaluates the type of the string.

# Method	True If
# .isalnum()	String consists of only alphanumeric characters
# .isalpha()	String consists of only alphabetic characters
# .isnumeric()	String consists of only numeric characters
# .islower()	String’s alphabetic characters are all lower case
# .isupper()	String’s alphabetic characters are all upper case
# .isspace()	String consists of only whitespace characters
# .istitle()	String is in title case

# create a new string
str1 = "Python4Beginners"

# Output: True
print(str1.isalnum())

# create a new string
str2 = "PythonForBeginners"

# Output: True
print(str2.isalpha())

# create a new string
str3 = "2019"

# Output: True
print(str3.isnumeric())

# create a new string
str4 = "emre"

# Output: True
print(str4.islower())

# create a new string
str5 = "EMRE"

# Output: True
print(str5.isupper())

# create a new string
str6 = " "

# Output: True
print(str6.isspace())

# create a new string
str7 = "Emre Bolat"

# Output: True
print(str7.istitle())


# String Length
# Built-in string method .len() returns the number of characters in a string.

# create a new string
emre = "emre.me"

# Output: 7
print(len(emre))


# .join(), .split() and .replace()
# .join(), .split() and .replace() are very useful methods for manipulating strings in Python.

# create a new string
str1 = "emre.me"
str2 = "emre"
str3 = "me"

# Output: e m r e . m e
print(" ".join(str1))

# Output: emre.me
print(".".join([str2, str3]))

# Output: ['emre', 'me']
print(str1.split("."))

# Output: emre-me
print(str1.replace(".", "-"))

# .strip(), .rstrip() and .lstrip()
# Returns a copy of the string with the leading .lstrip() and trailing .rstrip() whitespace removed. Method .strip() removes both.

# create a new string
str1 = "   emre.me   "

# Output: "emre.me   "
print(str1.lstrip())

# Output: "   emre.me"
print(str1.rstrip())

# Output: "emre.me"
print(str1.strip())


# .find() and .rfind()
# .find() method returns the index of the first found occurrence of the given subsequence searching from left-to-right. .rfind() method searches right-to-left.

# create a new string
str1 = "emre.me"

# Output: 1
print(str1.find("m"))

# Output: 5
print(str1.rfind("m"))


# .count()
# .count() method counts the number of occurrences of one string within another string.

# create a new string
str1 = "emre.me"

# Output: 3
print(str1.count("e"))
# With using three parameters .count(substring, left, right), the count is performed within the slice [left:right].

# create a new string
str1 = "emre.me"

# Output: 1
print(str1.count("e", 1, 6))
# Output is 1 because, by writing .count("e", 1, 6), we actually count the number of e characters in [1:6] split of emre.me, which is mre.m.
