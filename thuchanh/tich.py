def extended_euclidean(e, phi):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while phi != 0:
        q, e, phi = e // phi, phi, e % phi
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return e, x0, y0

def mod_inverse(e, phi):
    gcd, x, y = extended_euclidean(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

# Example calculation with p = 2357, q = 2551, e = 3674911
p = 2357
q = 2551
e = 3674911
phi = (p - 1) * (q - 1)

# Calculate modular inverse of e mod phi
d = mod_inverse(e, phi)
print("d =", d)

# Verify with e = 11
e_test = 11
d_test = mod_inverse(e_test, phi)
print("d_test =", d_test)
