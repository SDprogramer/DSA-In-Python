n = int(input("Enter a number = "))

def func(sum, i, n):
    if i > n:
        print("Sum =", sum)
        return
    func(sum + i, i + 1, n)

func(0, 1, n)