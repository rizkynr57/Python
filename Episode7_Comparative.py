#Operational Comparative
a = 4
b = 2
c = 3

#Lebih besar dari (>)
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = c > 3
print(c,">",3,"=",hasil)

print("\n")

#Kurang besar dari (<)
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = c < 3
print(c,"<",3,"=",hasil)

print("\n")

#Lebih dari sama dengan (>=)
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = c >= 3
print(c,">=",3,"=",hasil)

print("\n")

#Kurang dari sama dengan (<=)
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = c <= 3
print(c,"<=",3,"=",hasil)

print("\n")

#Sama dengan (==)
hasil = a == 3
print(a,"==",3,"=",hasil)
hasil = b == 3
print(b,"==",3,"=",hasil)
hasil = c == 3
print(c,"==",3,"=",hasil)

print("\n")

#Tidak sama dengan (!=)
hasil = a !=3
print(a,"!=",3,"=",hasil)
hasil = b !=3
print(b,"!=",3,"=",hasil)
hasil = c !=3
print(c,"!=",3,"=",hasil)

print("\n")

#Comparative object identity (is)
x = 5
y = 5
print("Nilai x =",x," ,id = ",hex(id(x)))
print("Nilai y =",y," ,id = ",hex(id(y)))
hasil = x is y
print("x is y = ",hasil)
x = 3
y = 4
hasil = x is y
print("x is y = ",hasil)

print("\n")

#Comparative object identity (is not)
x = 5
y = 5
print("Nilai x =",x," ,id = ",hex(id(x)))
print("Nilai y =",y," ,id = ",hex(id(y)))
hasil = x is not y
print("x is not y = ",hasil)
x = 3
y = 4
hasil = x is not y
print("x is not y = ",hasil)