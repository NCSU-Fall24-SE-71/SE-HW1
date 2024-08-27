"""
Function to identify if a given string str is a Palindrome or not.

Arguments: 
String - str

Returns:
True - if string is a valid Palindrome 
False - if string is not a valid Palindrome
"""
def isPalindrome(str):

    if str == str[::-1]:
        return True
    else:
        return False

palindromeString = 'racecar '
res = isPalindrome(palindromeString)

if res:
    print('The String ' + palindromeString + ' is a valid Palindrome.')
else:
    print('The String ' + palindromeString + ' is not a valid Palindrome.')