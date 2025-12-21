nums = [-1,0,1,2,-1,-4]
answer = []
nums.sort()
for i, a in enumerate(nums):
    if i> 0 and a == nums[i-1]:
        continue
    l, r = i+ 1, len(nums)-1
    while l< r:
        suma3 = a + nums[l] + nums[r]
        if 0 < suma3:
            r = r - 1 
        elif 0> suma3:
            l = l +1 
        else:
            answer.append([a, nums[l], nums[r] ])
            l += 1
            while nums[l] == nums[l-1] and l<r:
                l+=1
print(answer)