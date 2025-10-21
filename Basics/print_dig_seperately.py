n = int(input("Enter a number = "))
num = n
dig = []

if num == 0:
    print("The digit is 0")

while num > 0:
    last_dig = num % 10
    dig.append(last_dig)
    num = num // 10

print("The digits are = ", dig)