#Comparative and Logic(Boolean)

inputUser = float(input("Masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 = ")) 

isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan = ", isCorrect)

print("\n",10*"=", "\n")

inputUser = float(input("Masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 = "))

isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

isCorrect = isLebihDari and isKurangDari
print("Angka yang anda masukan = ",isCorrect)