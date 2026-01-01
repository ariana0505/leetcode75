height = [1,8,6,2,5,4,8,3,7]
l , r = 0 , len(height) - 1
cantidad_maxima = 0
while l < r:
    cantidad = min(height[l] , height[r]) * (r - l)
    cantidad_maxima = max(cantidad_maxima,cantidad)
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(cantidad_maxima)