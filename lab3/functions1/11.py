def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word=input()
print(is_palindrome(word))