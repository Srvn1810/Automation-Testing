# 1.what is the expected output of the following python code given below

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))
# note -the output would be a list containing the elements from the data list that are greater than 4.

# 2.write a python code using Lambda function to check every element of a list is an integer or string
# Sample list containing a mix of integers and strings
my_list = ['Water', 'apple', 'Computer']
my_list2 = [1,2,3,4,5,6,7,8,9,0]
is_integer = lambda x: isinstance(x, int)
is_string = lambda x: isinstance(x, str)
result_integers = all(map(is_integer, my_list2))
result_strings = all(map(is_string, my_list))
print(f"All elements are integers: {result_integers}")
print(f"All elements are strings: {result_strings}")

my_list3 =  [1, 'apple', 2, 'water']
result_strings = all(map(is_string, my_list3))
result_integers = all(map(is_integer, my_list3))
print(f"All elements are integers: {result_integers}")
print(f"All elements are strings: {result_strings}")

# 3.using the python lambda function create a fibonacci series from 1 to 50 elements?
from functools import reduce
num_elements = 50
fibonacci = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])
fibonacci_series = fibonacci(num_elements)
print(f"Fibonacci series with {num_elements} elements: {fibonacci_series}")

# 4. write a python function to validate the regular expression for the following ;-
# a.) email address
# b.) mobile number of bangladesh
# c.) Telephone number of USA
# d.) 16 character Alpha-Numeric Password composed of alphabets of
# upper case, lower case, special characters, numbers.

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def validate_bangladesh_mobile_number(mobile_number):
    pattern = r'^01[3-9]\d{8}$'
    return re.match(pattern, mobile_number) is not None

def validate_usa_telephone_number(telephone_number):
    pattern = r'^\d{3}-?\d{3}-?\d{4}$'
    return re.match(pattern, telephone_number) is not None

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return re.match(pattern, password) is not None

email = "example@email.com"
mobile_number = "01712345678"
telephone_number = "123-456-7890"
password = "Abcd1234@!5678"

print(f"Email is valid: {validate_email(email)}")
print(f"Bangladesh Mobile Number is valid: {validate_bangladesh_mobile_number(mobile_number)}")
print(f"USA Telephone Number is valid: {validate_usa_telephone_number(telephone_number)}")
print(f"Password is valid: {validate_password(password)}")

