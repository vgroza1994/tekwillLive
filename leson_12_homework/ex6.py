import re

def is_palindrome(text):
    cleaned_text = re.sub(r'[^a-zA-Z]', '', text.lower())
    return cleaned_text == cleaned_text[::-1]

text = input("Introdu textul: ")

if is_palindrome(text):
    print("Textul este un polindrom.")
else:
    print("Textul nu este un polindrom.")