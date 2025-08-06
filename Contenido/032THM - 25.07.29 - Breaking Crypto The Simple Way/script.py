from sympy import factorint
from Crypto.Util.number import inverse, long_to_bytes


n = 43941819371451617899582143885098799360907134939870946637129466519309346255747  
e = 65537  
c = 9002431156311360251224219512084136121048022631163334079215596223698721862766

# c = pow(m, e, n)
# m = pow(c, d, n)

'''
# used for factorization
factors = factorint(n)
p, q = factors.keys()
print("Prime factors:")
print("p =", p)
print("q =", q)
'''

p = 205237461320000835821812139013267110933
q = 214102333408513040694153189550512987959

phi_n = (p - 1) * (q - 1)

# Calculate the modular inverse of e modulo phi_n  (d = e^(-1) mod phi_n)
d = inverse(e, phi_n)
print("Private exponent d:", d)

# Decrypt the ciphertext
m = pow(c, d, n)
print("Decrypted message (as integer):", m)
print("Decrypted message (as bytes):", long_to_bytes(m))
# Output the decrypted message
print("Decrypted message (as string):", long_to_bytes(m).decode('utf-8', errors='ignore'))