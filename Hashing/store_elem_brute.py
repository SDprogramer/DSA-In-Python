'''
Constraints: 1 <= n[i] <= 10
No of elements in n = 10^8 and m = 10^8
'''

n = [1, 2, 5, 4, 3, 6, 8, 7, 9, 0, 10, 2, 5, 3, 6, 8, 7, 9, 0, 10]
m = [1, 2, 4, 4, 9, 7, 3, 7, 5, 5, 10, 3, 4, 9, 6]

for i in m:
    count = 0
    for j in n:
        if i == j:
            count += 1
    print(f"Element {i} occurs {count} times")

# T.C. = O(m*n) = 10^16
# S.C. = O(1)
