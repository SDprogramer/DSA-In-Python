n = int(input("Enter a number = "))
num = n
count = 0

if num == 0:
    print("The digit is 0")

while num > 0:
    last_dig = num % 10
    count += 1
    num = num // 10

print("The total number of digits are", count)

# T.C. = O(n)
# S.C. = O(1)

# See the python default function len() to count total digits in a number.