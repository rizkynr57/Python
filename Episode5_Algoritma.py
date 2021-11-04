#Algoritma
a = 11
b = 3

#Operasi Tambahan
hasil = a + b
print(a,"+",b, "=", hasil)

#Operasi Pengurangan
hasil = a - b
print(a,"-",b , "=" , hasil)

#Operasi Perkalian
hasil = a * b
print(a,"x",b , "=" , hasil)

#Operasi Pembagian
hasil = a / b
print(a,":",b , "=" , hasil)

#Operasi Eksponen(Pangkat)
hasil = a ** b
print(a,"xx",b, "=", hasil)

#Operasi Modulus
hasil = a % b
print(a,"%",b , "=", hasil)

#Operasi Floor Division
hasil = a // b
print(a,"::",b, "=", hasil)

#Operational Precedence
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x, "xx", y, "x",z, "+", x , ":", y, "-",y, "%",z, "::",x, "=", hasil)

hasil = x + y * z
print(x, "+", y, "x", z, "=", hasil)