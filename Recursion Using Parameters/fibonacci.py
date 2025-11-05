n = int(input("Enter a positive integer: "))

def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")