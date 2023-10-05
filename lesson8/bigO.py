n = int(input()) # O(1)
my_mult = 1 # O(1)
my_sum = 0 # O(1)
# O(3) == O(1)

n = 100000 # O(1)
nums = list(range(n+1)) # [0, 1, 2, 3, 4, ..., n] # O(n)
# O(1) + O(n) = O(n)

for num in nums: # O(n) # 100
    print(num) # O(1)
# O(n) * O(1) == O(n)


for k in range(2, n + 1): # O(n) # 100
    for m in range(2 * k, n + 1, k): # O(n-k) == O(n) # 100
        nums[m] = 0 # O(1)
# O(n) * O(n) == O(n**2) # 10000