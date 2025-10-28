n = int(input("Enter the number = "))

def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(i)

func(1, n)
