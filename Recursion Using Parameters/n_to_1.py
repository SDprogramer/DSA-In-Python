n = int(input("Enter the number = "))

def func(i):
    if i == 0:
        return
    print(i)
    func(i - 1)

func(n)
