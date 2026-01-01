 # Program to check palindrome

def is_palindrome(s):
    s = str(s)  
    return s == s[::-1]

word = input("Enter a word or number: ")
if is_palindrome(word):
    print(" It's a palindrome!")
else:
    print(" Not a palindrome.")
