nums = [9,6,4,2,3,5,7,0,1]
res = 0
for i in range(len(nums) + 1):
    res ^= i
for i in nums:
    res ^= i 
print(res)