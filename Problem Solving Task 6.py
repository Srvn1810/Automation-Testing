# 1. expected output of the below following

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))

# Output = [10, 501, 22, 37, 100, 999, 87, 351]

# 2. write a python code using lambda function to check every elements of a list is an integer or string?

elements = [1, 'hello', 3, 'world', 5]

check_elements = all(map(lambda x: isinstance(x, (int, str)), elements))

print(check_elements)

#  3. Using the python lambda function create a Fibonacci series from 1 to 50 elements/

from functools import reduce

n = 50

fibonacci_series = reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print(fibonacci_series)

# 4. Write a Python function to validate the regular expression for the following
#       a. email address
import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
#       B. Mobile number of Bangladesh
def validate_bangladesh_mobile(number):
    pattern = r'^(\+8801|8801|01)[3-9]\d{8}$'
    return bool(re.match(pattern, number))
#      C. Telephone number of USA
def validate_usa_telephone(number):
    pattern = r'^\+?1?\d{10}$'
    return bool(re.match(pattern, number))
#      D. 16 Character alphanumeric Password composed of alphabets of upper case lower case, special char, Numbers
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(pattern, password))

print(validate_email("example@example.com"))  # True
print(validate_bangladesh_mobile("+8801712345678"))  # True
print(validate_usa_telephone("+12345678901"))  # True
print(validate_password("Aa1!Aa1!Aa1!Aa1!"))  # True




