
print('----------------')
# Left shift <<
# X << Y
# Adds Y 0s at the end of X

print('X << Y operation:')
X  = 5
print('X =', bin(X))
print('Y = 2')
Y = 2
X = X << 2
print('X << Y =', bin(X))

print('----------------')


# Right shift >>
# X >> Y
# Removes Y bits from right side of X
print('X >> Y operation:')
X  = 5
print('X =', bin(X))
print('Y = 2')

X = X >> 2
print('X >> Y =', bin(X))

print('----------------')


# And operator (&)
# X & Y
print('X & Y operation:')

print('1 & 1 = ', bin(1 & 1))
print('1 & 0 = ', bin(1 & 0))
print('0 & 1 = ', bin(0 & 1))
print('0 & 0 = ', bin(0 & 0))

# Its same as True and True in python-conditions
print('----------------')


# Or operator (|)
# X | Y
print('X | Y operation:')

print('1 | 1 = ', bin(1 | 1))
print('1 | 0 = ', bin(1 | 0))
print('0 | 1 = ', bin(0 | 1))
print('0 | 0 = ', bin(0 | 0))

# Its same as True or True in python-conditions
print('----------------')


# 1's complement
# ~X
print("1's complement")

print(f'~ {bin(1)} = ', bin(~ 1))
print(f'~ {bin(0)} = ', bin(~ 0))

# Its same as True or True in python-conditions
print('----------------')


# XOR operation
# Simplified intuition:
# Let's assume X or Y = True. (assume that only either of them is True)
# and X ^ Y gives us X's condition (state) (whether it was considered or not)

# XOR always states whether X was True or False (X's complement)
# If Y is True, then according to our assumption, X was False.
# Hence, when Y is True, X ^ Y = X's complement
# When Y is False, then accoring to our assumption, X was True
# Hence, when Y is False, X ^ Y = X

print('X ^ Y operation:')

print('1 ^ 1 = ', bin(1 ^ 1))
print('1 ^ 0 = ', bin(1 ^ 0))
print('0 ^ 1 = ', bin(0 ^ 1))
print('0 ^ 0 = ', bin(0 ^ 0))

# X ^ X = 0 if X is not 0
# X ^ 0 = X

print('----------------')
