x = 10
y = 5

# penjumlahan
hasil = x + y 
print("Hasil tambah dari {a} + {b} = {hasil} ".format(a=x,b=y,hasil=hasil))
# pengurangan
hasil = x - y
print("Hasil kurang dari {0} - {1} = {2} ".format(x,y,hasil))
# perkalian 
hasil = x * y 
print("Hasil kali dari {a} * {b} = {hasil} ".format(hasil=hasil,a=x,b=y))
# pembagian 
hasil = x / y 
print("Hasil bagi dari {a} / {b} = {hasil} ".format(a=x,b=y,hasil=hasil))
#modulus
hasil = x % y
print("Hasil sisa bagi dari {a} % {b} = {hasil}".format(a=x,b=y,hasil=hasil))
# perpangkatan
hasil = x ** y
print("Hasil dari pangkat {a} ^ {b} = {hasil}".format(a=x,b=y,hasil=hasil))

nilai = 0
# nilai= nilai + 1
nilai += 1
print("Hasil dari nilai increment 0 = 0(old) + 1 : {nilai}".format(nilai=nilai))
nilai -= 1
print("Hasil dari nilai increment 1 = 1(old) - 1 : {nilai}".format(nilai=nilai))