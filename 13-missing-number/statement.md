# 🧩 13. Missing Number / Número faltante

## 🇬🇧 English Version

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the **only number in the range that is missing** from the array.

### 🧠 Examples

#### Example 1
```text
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 so numbers should be in [0,3]. 2 is missing.
```

#### Example 2
```text
Input: nums = [0,1]
Output: 2
```

#### Example 3
```text
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

### ⚙️ Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.

---

## 🇪🇸 Versión en Español

Dado un arreglo `nums` que contiene `n` números distintos en el rango `[0, n]`, devuelve el **único número del rango que falta** en el arreglo.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [3,0,1]
Salida: 2
Explicación: n = 3 entonces los números deben estar en [0,3]. 2 falta.
```

#### Ejemplo 2
```text
Entrada: nums = [0,1]
Salida: 2
```

#### Ejemplo 3
```text
Entrada: nums = [9,6,4,2,3,5,7,0,1]
Salida: 8
```

### ⚙️ Restricciones

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- Todos los números en `nums` son **únicos**.
## Missing Number (English)

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the **only number in the range that is missing** from the array.

### Example 1
**Input:** `nums = [3,0,1]`  
**Output:** `2`  

**Explanation:**  
`n = 3` since there are 3 numbers, so all numbers should be in the range `[0,3]`.  
`2` is the missing number because it does not appear in `nums`.

### Example 2
**Input:** `nums = [0,1]`  
**Output:** `2`  

**Explanation:**  
`n = 2` since there are 2 numbers, so all numbers should be in the range `[0,2]`.  
`2` is the missing number because it does not appear in `nums`.

### Example 3
**Input:** `nums = [9,6,4,2,3,5,7,0,1]`  
**Output:** `8`  

**Explanation:**  
`n = 9` since there are 9 numbers, so all numbers should be in the range `[0,9]`.  
`8` is the missing number because it does not appear in `nums`.

---

## Número Faltante (Español)

Dado un arreglo `nums` que contiene `n` números distintos en el rango `[0, n]`, devuelve el **único número del rango que falta** en el arreglo.

### Ejemplo 1
**Entrada:** `nums = [3,0,1]`  
**Salida:** `2`  

**Explicación:**  
`n = 3` ya que hay 3 números, por lo tanto todos deberían estar en el rango `[0,3]`.  
`2` es el número faltante porque no aparece en `nums`.

### Ejemplo 2
**Entrada:** `nums = [0,1]`  
**Salida:** `2`  

**Explicación:**  
`n = 2` ya que hay 2 números, por lo tanto todos deberían estar en el rango `[0,2]`.  
`2` es el número faltante porque no aparece en `nums`.

### Ejemplo 3
**Entrada:** `nums = [9,6,4,2,3,5,7,0,1]`  
**Salida:** `8`  

**Explicación:**  
`n = 9` ya que hay 9 números, por lo tanto todos deberían estar en el rango `[0,9]`.  
`8` es el número faltante porque no aparece en `nums`.
