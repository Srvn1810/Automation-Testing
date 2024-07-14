# 1. Separate Even and Odd Numbers

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# 2. Count and List Prime Numbers

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Find prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

print("Count of prime numbers:", len(prime_numbers))
print("Prime numbers:", prime_numbers)

# 3. Count Happy Numbers

# Helper function to check if a number is a happy number
def is_happy_number(n):
    def get_next(number):
        return sum(int(char) ** 2 for char in str(number))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1


# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Find happy numbers
happy_numbers = [num for num in numbers if is_happy_number(num)]

print("Count of happy numbers:", len(happy_numbers))
print("Happy numbers:", happy_numbers)

# 4. Sum of the First and Last Digit of an Integer

# Function to find the sum of the first and last digit of an integer
def sum_first_last_digit(n):
    digits = str(n)
    first_digit = int(digits[0])
    last_digit = int(digits[-1])
    return first_digit + last_digit

# Example usage
num = 12345
print("Sum of first and last digit:", sum_first_last_digit(num))

# 5. Distribute Mangoes to Minimize Difference

# Function to minimize the difference between the maximum and minimum mangoes in bags
def minimize_mango_difference(mangoes, students):
    mangoes.sort()
    min_difference = float('inf')
    for i in range(len(mangoes) - students + 1):
        current_difference = mangoes[i + students - 1] - mangoes[i]
        min_difference = min(min_difference, current_difference)
    return min_difference

# Example usage
mangoes = [10, 20, 30, 40, 50, 60]
students = 3
print("Minimum difference:", minimize_mango_difference(mangoes, students))

# 6. Find Duplicates in Three Lists

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

# Find duplicates
duplicates = set(list1) & set(list2) & set(list3)

print("Duplicates in the three lists:", list(duplicates))

# 7. Find the First Non-Repeating Element in a List

# Example list
numbers = [2, 3, 4, 2, 3, 5, 4, 6]

# Function to find the first non-repeating element
def first_non_repeating(lst):
    from collections import Counter
    count = Counter(lst)
    for num in lst:
        if count[num] == 1:
            return num
    return None

# Find the first non-repeating element
first_unique = first_non_repeating(numbers)

print("First non-repeating element:", first_unique)


# 8. Find the Minimum Element in a Rated and Sorted List

# Given a rated and sorted list
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Minimum element in a sorted list is always the first element
minimum_element = sorted_list[0]

print("Minimum element:", minimum_element)

# 9. Find a Triplet in the List Whose Sum is Equal to the Given Value

# Given list and target value
numbers = [10, 20, 30, 9, 29]
target_sum = 59

# Function to find triplets with the given sum
def find_triplet(lst, target):
    n = len(lst)
    lst.sort()
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            if current_sum == target:
                return lst[i], lst[left], lst[right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None

# Find the triplet
triplet = find_triplet(numbers, target_sum)

print("Triplet with the given sum:", triplet)

# 10. Find if there is a Sub-list with Sum Equal to Zero

# Given list
numbers = [4, 2, -3, 1, 6]

# Function to check if a sub-list with sum zero exists
def has_sublist_with_sum_zero(lst):
    current_sum = 0
    seen_sums = set()
    for num in lst:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)
    return False

# Check for sub-list with sum zero
sublist_exists = has_sublist_with_sum_zero(numbers)

print("Sub-list with sum zero exists:", sublist_exists)


