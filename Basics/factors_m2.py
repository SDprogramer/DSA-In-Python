n = int(input("Enter a number: "))
factors = []

# Run a for loop from 1 to n and see which number is divisible by 20 and gives remainder zero
for i in range(1, n // 2):
    if n % i == 0:
        factors.append(i)

factors.append(n)  # Including n itself as a factor

print(f"The factors of {n} are: {factors}")

# T.C. = O(n/2)
# S.C. = O(k) where k is the total number of factors of n (Size of the list)