from sympy.ntheory.modular import crt

print(crt([99, 97, 95], [49, 76, 65]))
print(crt([643, 419, 733], [14, 254, 87], check=False))
print(crt([7, 13, 59, 31, 19],[0, 13-1, 59-4, 31-6, 19-7]))

for x in [7, 13, 59, 31, 19]:
    print(x, 2093560 % x)
    print(x, 1068781 % x)
