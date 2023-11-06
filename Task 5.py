#1.write a phyton program to calculate the total number of Vowels and counts of each individual vowel AEIOU
String = input('Enter the string :')
count = 0
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))

#2.create a pyramid of numbers 1 to 20
for i in range(1, 22):
    for j in range(22 - i):
        print(" ", end=" ")
    for j in range(1, i):
        print(j, end=" ")
    print("\n")

#3.write a function that takes a string and returns a new string with all the vowels removed
string = "aeioustesting"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]
print("\nAfter removing Vowels: ", result)

#4.write a function that takes a string and returns the number of unique characters in it
name = 'saravanan yoganandham jayanthi yoganandham harshitha yoganandham'
unique_words = set(name.split())
print(unique_words)
length = len(unique_words)
print(length)

#5.write a function that takes a string and returns true if it is a palindrome and false otherwise
def is_palindrome(input_string):
    clean_string = input_string.replace(" ", "").lower()

    return clean_string == clean_string[::-1]
#True
input_string = "nurses run"
result = is_palindrome(input_string)
print(result)
#False
input_string2= "A Man"
result = is_palindrome(input_string2)
print(result)

#6.write a function that takes two string and return the longest common substring between them
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    longest_substring = str1[end_index - max_length:end_index]

    return longest_substring

str1 = "saravanan yoganandham"
str2 = "jayanthi yoganandham"
result = longest_common_substring(str1, str2)
print(result)

#7.write a function that takes a string and return the most frequent character in it
def most_frequent_character(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_frequent_char = max(char_count, key=char_count.get)

    return most_frequent_char

input_str = "Saravanan Yoganandham!"
result = most_frequent_character(input_str)
print(result)

#8.write a function that takes a string and returns true if it is an anagram of another string, false otherwise
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)
#True
string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print(result)
#false
string1 = "list"
string2 = "lent"
result = is_anagram(string1, string2)
print(result)

#9.write a function that takes a string and returns number of words in it
def count_words(input_string):
    words = input_string.split()
    return len(words)

input_str = "A man with a plan right here."
result = count_words(input_str)
print(result)  # Output: 7
