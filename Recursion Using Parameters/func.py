def say_hello(x, N):
    if N == 0:
        return
    print(x)
    say_hello(x, N - 1)

say_hello(21, 6)

# T.C. = O(n)
# S.C. = O(n) due to call stack usage
