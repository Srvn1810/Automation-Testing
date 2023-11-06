#1.You have been given a python list [10, 501, 22, 37, 100, 999, 87, 351]
# your task is to create two list one which have all the even number and another list which will have all the odd numbers in it?
number_list= [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = []
odd_numbers = []
for number in number_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#2.given a python list [10, 501, 22, 37, 100, 999, 87, 351] your task is to count all the prime numbers
# and create a new python list which will contain all the prime numbers in it?
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
number_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = []
for number in number_list:
    if is_prime(number):
        prime_numbers.append(number)
print("Prime numbers:", prime_numbers)

#3.given a python list [10, 501, 22, 37, 100, 999, 87, 351]
# find out how many numbers are there in the given python list which are happy numbers?
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
original_list = [10, 501, 22, 37, 100, 999, 87, 351]
count_happy_numbers = 0
for number in original_list:
    if is_happy_number(number):
        count_happy_numbers += 1
print("Number of happy numbers:", count_happy_numbers)

#4.write a python program to find the sum of the first and last digit of an integer?
num = int(input("Enter an integer: "))
num_str = str(num)
first_digit = int(num_str[0])
last_digit = int(num_str[-1])
sum_of_digits = first_digit + last_digit
print(f"The sum of the first and last digits of {num} is {sum_of_digits}")

#5.
def distribute_mangoes(mangoes, students):
    if students > len(mangoes):
        return "Not enough bags for students"
    mangoes.sort()
    min_diff = float('inf')
    for i in range(len(mangoes) - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff
mangoes = [9, 8, 13, 16, 14, 1]
students = 5
result = distribute_mangoes(mangoes, students)
print(f"The minimum difference is {result}")

#6.you have been given three lists. your task is to find the duplicates in the three lists.
# write a python program for the same. you can use your own python list
list1 = [18, 20, 35, 45, 65, 75, 60]
list2 = [45, 15, 60, 75, 18]
list3 = [65, 60, 45, 100]
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
common_elements = set1.intersection(set2, set3)
common_elements_list = list(common_elements)
print("Common elements in the three lists:", common_elements_list)

#7.
def find_first_non_repeating_element(numbers):
    element_count = {}
    for number in numbers:
        if number in element_count:
            element_count[number] += 1
        else:
            element_count[number] = 1
    for number in numbers:
        if element_count[number] == 1:
            return number
    return None

numbers = [12, 13, 14, 12, 13, 15, 16, 41, 27]

first_non_repeating = find_first_non_repeating_element(numbers)
if first_non_repeating is not None:
    print("The first non-repeating element is:", first_non_repeating)
else:
    print("There are no non-repeating elements in the list.")

#8.write a python program to find the minimum element in a rated and sorted list?
def find_minimum_element(sorted_list):
    if not sorted_list:
        return None
    return sorted_list[0]
sorted_list = [20, 50, 30, 44, 52, 69]
minimum_element = find_minimum_element(sorted_list)
if minimum_element is not None:
    print("The minimum element is:", minimum_element)
else:
    print("The list is empty.")

#10.given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with sum equal to Zero?
def has_sublist_with_zero_sum(arr):
    prefix_sum_set = set()
    prefix_sum = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in prefix_sum_set:
            return True
        prefix_sum_set.add(prefix_sum)
    return False
arr = [4, 2, -3, 1, 6]
if has_sublist_with_zero_sum(arr):
    print("There is a sub-list with a sum of zero.")
else:
    print("There is no sub-list with a sum of zero.")









