'''
Constraints: 1 <= n[i] <= 10
No of elements in n = 10^8 and m = 10^8
'''

n = [1, 2, 5, 4, 3, 6, 8, 7, 9, 0, 10, 2, 5, 3, 6, 8, 7, 9, 0, 10]
m = [1, 2, 4, 4, 9, 7, 3, 7, 5, 5, 10, 3, 4, 9, 6]
n_len = len(n)
m_len = len(m)
hash_dict = {} # Using dictionary to store counts

for i in range(0, n_len):
    hash_dict[n[i]] = hash_dict.get(n[i], 0) + 1
for j in range(0, m_len):
    count = hash_dict.get(m[j], 0)
    print(f"Element {m[j]} occurs {count} times")

# T.C. = O(n + m) = 2*10^8
# S.C. = O(n)