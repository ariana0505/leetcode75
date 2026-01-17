# Lista de números de ejemplo
nums = [10, 9, 2, 5, 3, 7, 101, 18]

# Creamos la lista LIS con valor inicial 1 en cada posición
# (cada número por sí solo es una subsecuencia de longitud 1)
LIS = [1] * len(nums)

# Recorremos la lista desde el final hacia el inicio
for i in range(len(nums) - 1, -1, -1):

    # Recorremos los elementos que están a la derecha de i
    for j in range(i + 1, len(nums)):

        # Si el número en i es menor que el número en j
        if nums[i] < nums[j]:

            # Actualizamos el mejor valor posible para LIS[i]
            LIS[i] = max(LIS[i], 1 + LIS[j])

# Mostramos la longitud de la subsecuencia creciente más larga
print(max(LIS))
