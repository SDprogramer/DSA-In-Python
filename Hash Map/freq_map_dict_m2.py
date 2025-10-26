nums = [2, 4, 2, 3, 4, 4, 5, 2, 7, 7, 8, 2, 3, 9, 10]
hash_map = {} # An empty dictionary to store frequency counts
n = len(nums)
for i in range(0, n): # O(n)
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1 # O(1)

print("Frequency map:", hash_map)

# T.C. O(n) where n is the number of elements in the nums list
# S.C. O(n)
