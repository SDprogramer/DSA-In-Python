from math import sqrt

n = int(input("Enter a number: "))
factors = []

# Run a for loop from 1 to sqrt(n) and see which number is divisible by n and gives remainder zero
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        factors.append(i);
        if n // i != i:
            factors.append(n // i)

factors.sort() # T.C. = O(k log k) to sort the factors

print(f"The factors of {n} are: {factors}")

# T.C. = O(sqrt(n))
# S.C. = O(k) where k is the total number of factors of n (Size of the list)
