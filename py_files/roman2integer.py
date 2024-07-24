# LeetCode Roman Number to Integer
# Date: 6/14-15/2024
# Given a number Roman String, turn into an integer. 
# Runtime 51 ms (Slow compared to others)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize total and previous value
        total = 0
        prev_value = 0

        # Iterating through the string in reverse order
        for char in reversed(s):
            value = roman_values[char]

            # Print the character and its value for debugging
            print("Character: {}, Value: {}".format(char, value))

            # If the current value is less than the previous value, subtract it from total
            if value < prev_value:
                total -= value
            else:
                total += value

            # Update the previous value
            prev_value = value

        return total
        
# Example usage
solution = Solution()
print(solution.romanToInt("III"))    # Output: 3
print(solution.romanToInt("IV"))     # Output: 4
print(solution.romanToInt("IX"))     # Output: 9
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))# Output: 1994
