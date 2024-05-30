# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
#
# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#
# >>> print 'ab123'.isalnum()
# True
# >>> print 'ab123#'.isalnum()
# False
# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
#
# >>> print 'abcD'.isalpha()
# True
# >>> print 'abcd1'.isalpha()
# False
# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).
#
# >>> print '1234'.isdigit()
# True
# >>> print '123edsd'.isdigit()
# False
# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).
#
# >>> print 'abcd123#'.islower()
# True
# >>> print 'Abcd123#'.islower()
# False
# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).
#
# >>> print 'ABCD123#'.isupper()
# True
# >>> print 'Abcd123#'.isupper()
# False

# Output Format
#
# In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if s has any alphabetical characters. Otherwise, print False.
# In the third line, print True if s has any digits. Otherwise, print False.
# In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if s has any uppercase characters. Otherwise, print False.


s = input()
isAlphanumeric = False
isAlphabetical = False
isDigits = False
isLowercase = False
isUppercase = False

for i in s:
    if i.isalnum():
        isAlphanumeric = True
    if i.isalpha():
        isAlphabetical = True
    if i.isdigit():
        isDigits = True
    if i.islower():
        isLowercase = True
    if i.isupper():
        isUppercase = True

print(isAlphanumeric)
print(isAlphabetical)
print(isDigits)
print(isLowercase)
print(isUppercase)



