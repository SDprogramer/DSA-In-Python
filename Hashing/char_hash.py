'''
Constraints: 'a' <= n[i] <= 'z'
No of elements in n = 10^8 and m = 10^8
'''

n = "sfdifisidisexydiyaiwillfuckarannikahiueaifksdbf"
m = ['s', 'f', 'g', 'i', 'q', 'e', 's']
n_len = len(n)
m_len = len(m)
hash_list = [0] * 26 # Since elements are in the range 0 to 26

for ch in n:
    idx = ord(ch) - ord('a')
    hash_list[idx] += 1
for ch in m:
    idx = ord(ch) - ord('a')
    if idx < 0 or idx > 25:
        print(f"Element {ch} occurs 0 times")
    else:
        print(f"Element {ch} occurs {hash_list[idx]} times")

# T.C. = O(n + m) = 2*10^8
# S.C. = O(1) # Since hash_list size is constant (26)