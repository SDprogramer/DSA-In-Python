count = 0

def say_hello():
    global count
    if count == 4:
        return
    count += 1
    say_hello()
    print("Hello, World!")

say_hello()

# T.C. = O(n)
# S.C. = O(n) due to call stack usage