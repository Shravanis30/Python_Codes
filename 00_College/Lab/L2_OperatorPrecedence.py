# Python Operator Precedence Demonstration

# Defining variables
a, b, c, d, e = 5, 3, 2, 10, 4
my_list = [1, 2, 3, 4, 5]

# all operator precedence rules
result = (lambda x: x ** 2)((a + b) * c) // d % e + ~(-b) << 1 & 7 | (3 ^ 2) and (not (a > b)) or (c if b in my_list else e)


print("Final Result:", result)



# Explaination
# (a + b) * c  → (5 + 3) * 2  → 8 * 2  → **16**

# (lambda x: x ** 2)(16) → **16² = 256**

# 256 // d → 256 // 10 → **25**
# 25 % e → 25 % 4 → **1**

# - b → -3
# ~(-b) → ~( -3 ) → ~( 3 ) → -4

# 3 ^ 2 → 3 XOR 2 → **1**  (Binary: `11 ^ 10 = 01`)

# -4 << 1  → **(-4 * 2) = -8**

# -8 & 7  → Binary: `11111000 & 00000111` → **0**

# 0 | 1 → **1**

# a > b → 5 > 3 → **True**
# not (a > b) → not (True) → **False**

# 1 and False → **False**

# b in my_list → 3 in [1, 2, 3, 4, 5] → **True**

# c if True else e → **2**

# False or 2 → **2**
