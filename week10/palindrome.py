def is_palindrome(s):
    clear_s = ''.join(char.lower() for char in s if char.isalnum())
    return clear_s == clear_s[::-1]
