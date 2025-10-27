'''
Constraints: 1 <= n[i] <= 10
No of elements in n = 10^8 and m = 10^8
'''

n = [1, 2, 5, 4, 3, 6, 8, 7, 9, 0, 10, 2, 5, 3, 6, 8, 7, 9, 0, 10]
m = [1, 2, 4, 4, 9, 7, 3, 7, 5, 5, 10, 3, 4, 9, 6]
n_len = len(n)
m_len = len(m)
hash_list = [0] * 11 # Since elements are in the range 0 to 10

for i in n:
    hash_list[i] += 1

for j in m:
    if j < 1 or j > 10:
        print(f"Element {j} occurs 0 times")
    else:
        print(f"Element {j} occurs {hash_list[j]} times")

# T.C. = O(n + m) = 2*10^8
# S.C. = O(1) # Since hash_list size is constant (11)
