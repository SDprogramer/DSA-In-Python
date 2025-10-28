count = 0

def say_hello():
    global count
    if count == 4:
        return
    print("Hello, World!")
    count += 1
    say_hello()

say_hello()

# T.C. = O(n)
# S.C. = O(n) due to call stack usage
