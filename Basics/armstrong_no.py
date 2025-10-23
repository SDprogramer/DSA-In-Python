n = int(input("Enter a number = "))
num = n
len = 0
dig = 0

if num == 0:
    print("The digit is 0")

# Finding the length of the number
while num > 0:
    last_dig = num % 10
    len = len + 1
    num = num // 10
print(f"The length of the number is {len}")

# Calculating the Armstrong number
num = n
while num > 0:
    last_dig = num % 10
    power = last_dig ** len
    dig = dig + power
    num = num // 10

if n == dig:
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")

# T.C. = O(d) where d is the number of digits in the number
# S.C. = O(1)