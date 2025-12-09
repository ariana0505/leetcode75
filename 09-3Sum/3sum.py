nums = [1,4,3,2,-5,-4,-8,6]
res = []
nums.sort()
for i , a in enumerate(nums):
    if i>0 and a == nums[i-1]:
        continue
    l , r = i + 1, len(nums)-1
    while l < r:
        suma3 = a + nums[l]+ nums[r]
        if suma3 < 0:
            l += 1
        elif suma3 > 0:
            r -= 1
        else:
            res.append([a,nums[l],nums[r]])
            l += 1
            while nums[l] == nums[l-1] and l < r:
                l += 1
print(res)