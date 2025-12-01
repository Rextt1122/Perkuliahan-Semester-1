a = 0b01 #desimal=1
b = 0b10 #desimal=2

print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)

a = 4
b = 5

# Operasi AND
c = a & b
print("a & b = %s" % c)

# Operasi OR
c = a | b
print("a | b = %s" % c)

# Operasi XOR
c = a ^ b
print("a ^ b = %s" % c)

# Operasi Not
c = ~a
print("~a = %s" % c)

# Operasi shift left (tukar posisi biner)
c = a << b
print("a << b = %s" % c)

# Operasi shift right (tukar posisi biner)
c = a >> b
print("a >> b = %s" % c)