
def is_palindrome_number(num):
    num_str = str(num) # from Int to Str
    return num_str == num_str[::-1]

print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
