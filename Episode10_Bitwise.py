a = 9
b = 5
#OR (|)
c = a | b
print("Nilai : ", a,", binary : ", format(a,"08b"))
print("Nilai : ", b,", binary : ", format(b,"08b"))
print(31*"=")
print("Nilai : ", c,", binary : ", format(c,"08b"))
print("\n")
#AND (&)
c = a & b
print("Nilai : ", a,", binary : ", format(a,"08b"))
print("Nilai : ", b,", binary : ", format(b,"08b"))
print(31*"=")
print("Nilai : ", c,", binary : ", format(c,"08b"))
print("\n")
#XOR (^)
c = a ^ b
print("Nilai : ", a,", binary : ", format(a,"08b"))
print("Nilai : ", b,", binary : ", format(b,"08b"))
print(31*"=")
print("Nilai : ", c,", binary : ", format(c,"08b"))
#NOT (~)
c = ~a
print("\n")
print("Nilai : ",a,", binary : ", format(a, "08b"))
print(31*"=")
print("Nilai : ", c,", binary : ", format(c,"08b"))
#Shift Right
c = a >> 2
print("\n")
print("Nilai : ",a,", binary : ", format(a, "08b"))
print(31*"=")
print("Nilai : ", c,", binary : ", format(c,"08b"))
#Shift Left
c = a << 2
print("\n")
print("Nilai : ",a,", binary : ", format(a, "08b"))
print(31*"=")
print("Nilai : ", c,", binary : ", format(c,"08b"))