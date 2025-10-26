nums = [2, 4, 2, 3, 4, 4, 5, 2, 7, 7, 8, 2, 3, 9, 10]
freq_map = {} # An empty dictionary to store frequency counts

n = int(input("Enter the number to search frequency for: "))

for i in range(0, len(nums)): # O(n)
    num = nums[i]
    if num in freq_map: # O(1)
        freq_map[num] += 1 # O(1)
    else:
        freq_map[num] = 1 # O(1)

print("Frequency map:", freq_map)
print("The number", n, "appears", freq_map[n], "times in the list.")

# T.C. O(n) where n is the number of elements in the nums list
# S.C. O(n)
