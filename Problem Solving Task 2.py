# 1.  Write a python Program to calculate the total number of vowels and count of each individual
# vowel A E I O U in the string "Guvi Geeks Network Private Limited"

def count_vowels(s):
    # Initialize a dictionary to store counts of each vowel
    vowels = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

    # Convert the string to upper case to handle case insensitivity
    s = s.upper()

    # Initialize total vowels count
    total_vowels = 0

    # Iterate through each character in the string
    for char in s:
        if char in vowels:
            vowels[char] += 1
            total_vowels += 1

    return total_vowels, vowels
# Given string
string = "Guvi Geeks Network Private Limited"

# Count vowels
total_vowels, vowel_counts = count_vowels(string)

# Print the results
print("Total number of vowels:", total_vowels)
for vowel, count in vowel_counts.items():
    print(f"Count of {vowel}: {count}")



# 2. Create Pyramid of number from 1 to 20 using for loop
def print_pyramid(n):
    number = 1
    for i in range(1, n + 1):
        # Print leading spaces
        for _ in range(n - i):
            print(" ", end=" ")
        # Print numbers
        for j in range(1, i + 1):
            if number > 20:
                break
            print(number, end=" ")
            number += 1
        print()  # Move to the next line
        if number > 20:
            break
# Number of rows for the pyramid
rows = 6  # You can adjust this as needed, but for 1 to 20, 6 rows are enough
print_pyramid(rows)

# 3. Write a program that takes a string and returns a new string with all the vowels removed.

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

# Example usage
print(remove_vowels("Hello World"))  # Output: "Hll Wrld"

# 4.Write a program that takes a string and returns the number of unique characters in it.\

def count_unique_characters(s):
    return len(set(s))

# Example usage
print(count_unique_characters("Hello World"))  # Output: 8

# 5.Write a program that takes a string and returns True if it is a palindrome, False otherwise.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # Output: True

# 6.Write a program that takes two strings and returns the longest common substring between them.

def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0
    end = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end = i

    return s1[end - length:end]

# Example usage
print(longest_common_substring("abcdef", "zabcf"))  # Output: "abc"

# 7. Write a program that takes a string and returns the most frequent character in it.

def most_frequent_character(s):
    from collections import Counter
    count = Counter(s)
    return max(count, key=count.get)

# Example usage
print(most_frequent_character("Hello World"))  # Output: "l"

# 8. Write a program that takes a string and returns True if it is an anagram of another string, False otherwise.

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
print(is_anagram("listen", "silent"))  # Output: True

# 9. Write a program that takes a string and returns the number of words in it.

def count_words(s):
    return len(s.split())

# Example usage
print(count_words("Hello World, this is a test."))  # Output: 6







