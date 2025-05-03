# LeetCode Palindrome Problem Solution 
# Date: 6/13/2024
# Given a number, determine if it is a palindrome. A palindrome number reads the same forwards and backwards.

def is_palindrome_number(num):
    num_str = str(num) # from Int to Str
    return num_str == num_str[::-1]  # Check if the string 'num_str' is equal to its reverse (i.e., check if 'num_str' is a palindrome)

print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
