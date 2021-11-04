#Operational Logic (NOT)
a = True
c = not a
print("Data Boolean A = ", a)
print("Data Boolean C = ", c)

print("\n")

#Operational Logic (OR)
#Note : Jika keduanya False maka hasilnya False dan sisanya True
a = False
b = False
c = a or b
print(a,"OR",b,"=", c)
a = False
b = True
c = a or b
print(a,"OR",b,"=", c)
a = True
b = False
c = a or b
print(a,"OR",b,"=", c)
a = True
b = True
c = a or b
print(a,"OR",b,"=", c)

print("\n")

#Operational Logic (AND)
#Note : Jika keduanya True maka hasil True dan sisanya False
a = False
b = False
c = a and b
print(a,"AND",b,"=", c)
a = False
b = True
c = a and b
print(a,"AND",b,"=", c)
a = True
b = False
c = a and b
print(a,"AND",b,"=", c)
a = True
b = True
c = a and b
print(a,"AND",b,"=", c)

print("\n")

#Operational Logic (XOR)
#Note : Jika salah satunya true maka hasilnya true dan sisanya akan false
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=", c)
a = False
b = True
c = a ^ b
print(a,"XOR",b,"=", c)
a = True
b = False
c = a ^ b
print(a,"XOR",b,"=", c)
a = True
b = True
c = a ^ b
print(a,"XOR",b,"=", c)