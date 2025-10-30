n = int(input("Enter a number for factorial = "))

def func(factorial, i, n):
    if i > n:
        print("Factorial =", factorial)
        return
    func(factorial * i, i + 1, n)

func(1, 1, n)