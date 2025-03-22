#Q1 Check Palindrome
def check_palindrome(string):
    rev_str = string[::-1]
    if len(string) <= 2:
        return "String must have two characters at least "
    elif string == rev_str:
        return "Yes"
    else:
        return "No"
string = input('Enter a string: ')
result = check_palindrome(string)
print(result)
