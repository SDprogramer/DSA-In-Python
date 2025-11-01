def palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s, left + 1, right - 1)

s = "madam"
if palindrome(s, 0, len(s) - 1):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# T.C. = O(n)
# S.C. = O(n) (recursive stack space)