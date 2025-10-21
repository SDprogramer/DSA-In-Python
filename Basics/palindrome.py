n = int(input("Enter a number = "))
num = n
dig = 0

if num == 0:
    print("The digit is 0")

while num > 0:
    last_dig = num % 10
    dig = dig * 10 + last_dig
    num = num // 10

if n == dig:
    print(f"{n} is a palindrome")

# T.C. = O(d) where d is the number of digits in the number
# S.C. = O(1)