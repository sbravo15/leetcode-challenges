# LeetCode Roman Number to Integer
# Date: 6/14-15/2024
# Given a number Roman String, turn into an integer. 

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Values In a Dictionary:
roman_str = "IV"

roman_values = {
    'I': 1, 
    'V': 5,
    'X': 10,
    'L': 50, 
    'C': 100,
    'D': 500,
    'M': 1000
}

# Iterating through the string and printing corresponding values
for char in roman_str: 
    if char in roman_values: 
        print(f"Character: {char}, Value: {roman_values[char]}")
    else: 
        print(f"Character: {char} is not a valid Roman numeral")

# Calculating the integer value
total = 0
prev_value = 0 

for char in roman_str: 
    value = roman_values[char]
    total += value
    if value > prev_value:
        total -= 2 * prev_value
    prev_value = value

print("Integer value:", total)
