num = [1, 2, 4, 4, 9, 7, 3, 7, 5, 5, 10, 3, 4, 9, 6]
n = len(num)
left = 0
right = n - 1

def reverse(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse(arr, l + 1, r - 1)

reverse(num, left, right)
print(num)

# T.C. = O(n)
# S.C. = O(n) (recursive stack space)
