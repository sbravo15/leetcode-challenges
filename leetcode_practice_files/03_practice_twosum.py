# Create a list of five different Fruits: 
Fruits = ["Apple","Banana","Kiwi","Strawberry","Mango"]

first_fruit = Fruits[0]
last_fruit = Fruits[4]

# for fruit in Fruits:
#     print(fruit)

# Nested Loop
# for i in range(len(Fruits)):
#     for j in range(i + 1, len(Fruits)):
#         if Fruits[i] and Fruits[j] 
#         print(Fruits[i],Fruits[j])

numbers = [3, 2,  4]
target = 6
result = []
indices = []
for i in range(len(numbers)):
    for j in range(i +1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            indices.append(i)
            indices.append(j)
            result.append(numbers[i])
            result.append(numbers[j])
        else:
            pass

print(sum(result))
print(indices)

# Find the sum of all the multiples of 3 or 5 below 1000
# multiples = []
# for num in range(1000):
#     if num % 3 == 0 or num % 5 == 0:
#         multiples.append(num)
#     else: 
#         pass
# def sum_list():
#     return print(sum(multiples))

# sum_list()

#
# def fibonacci(n):
#     sequence = []
#     a, b = 0, 1
#     while len(sequence) < n:
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence

# # Example usage
# n_terms = 10
# print(fibonacci(n_terms))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# def fibonacci(n):
#     sequence = []
#     a, b = 0, 1
#     while len(sequence) < n: 
#         sequence.append(a) #adds the number into the fibonacci series list
#         a, b = b, a + b #Fibonacci
#     return sequence


# Methods viewed: len() : returns the lenght of the list, list.append(j) : appends just the index, list.append([j]) : appends the value inside the index
# sum() : returns all the sumation of values