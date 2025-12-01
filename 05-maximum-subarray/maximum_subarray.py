nums = [-2,1,-3,4,-1,2,1,-5,4]

maxSub = nums[0]
sumaActual = 0

for i in range(len(nums)):
    # Sumamos el valor actual
    sumaActual += nums[i]
    
    # Actualizamos el máximo
    maxSub = max(maxSub, sumaActual)
    
    # Si la suma acumulada cae debajo de 0, la reiniciamos
    if sumaActual < 0:
        sumaActual = 0

print(maxSub)
