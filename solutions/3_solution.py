def check_palindrome(n):
    temp = n
    rev = 0
    is_palindrome = False
    while (n != 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if temp == rev:
        is_palindrome = True
    return is_palindrome

n = int(input("Enter any number: "))
ans = check_palindrome(n)
if ans == True:
    print("The given number is a palindrome!")
else:
    print("The given number is not a palindrome!")
