nums = [-2,1,-3,4,-1,2,1,-5,4]

maxSub = nums[0]
sumaActual = 0

for i in range(len(nums)):
    sumaActual += nums[i]        # sumamos el valor actual
    
    if sumaActual < 0:           # si la suma cae a negativa, reiniciamos
        sumaActual = 0
    
    maxSub = max(maxSub, sumaActual)

print(maxSub)