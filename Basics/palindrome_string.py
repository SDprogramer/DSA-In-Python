str = "dhfsibiregsexynosheghddadsnfrsgeadngnisfka"
n = len(str)
left = 0
right = n - 1

while left < right:
    if str[left] != str[right]:
        print("The string is not a palindrome")
        break
    left += 1
    right -= 1

else:
    print("The string is a palindrome")

# T.C = O(n)
# S.C = O(1)