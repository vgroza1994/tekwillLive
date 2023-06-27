def check_palindrome(string):
    if not string:
        raise ValueError("Input string cannot be empty.")
    return string == string[::-1]
word = "level"
print(check_palindrome(word))

not_palindrome = "hello"
print(check_palindrome(not_palindrome))

empty_string = ""
print(check_palindrome(empty_string)) 