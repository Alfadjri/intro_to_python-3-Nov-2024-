#membuat list (Create)
#primsip programming (CRUD) Create , Read , Update , Delete
fruits = ["apple","pisang","salak","semangka"]
#mencetak semua nilai (Read)
print("=== Mencetak semua nilai ===") 
print(fruits) 
#mencetak salah satu nilai
#namaVariabel[posisi_value]
#contoh semangka
print("=== mencetak nilai posisi ke 3 ===")
print(fruits[2])
#misal nilainya min 
# print nilai terakhir
print("=== mencetak nilai akhir dari list ===")
print(fruits[-1]) 
#menambahkan nilai (Update)
print("=== menambahkan nilai list ===")
fruits.append("jeruk") 
print(fruits)
# menghapus nilai (Delete)
print("=== menghapus nilai nilai list ===")
fruits.remove("pisang")
print(fruits)
print("=== menggubah nilai list value jeruk menjadi mangga ===")
fruits[2] = "mangga"
print(fruits)
print("=== Reset Nilai ===")
fruits.remove("mangga")
fruits.remove("jeruk")
print(fruits)


print("=== menambah 2 data atau lebih ===")
buah = ["tomat","alpukat"]
# fruits = fruits + buah
fruits += buah
print(fruits)
