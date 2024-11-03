# Inisiliasi Data
# format dasar
# nama_variable = { key:value , key1:value2 }
biodata_simple = {
    "nama" : "Alfadjri Dwi Fadhilah",
    "age" : 24,
    "tempat_lahir" : "Bandung"
}

#  cetak nilai
print(biodata_simple)

# mengambil nilai spesifik
# biodata_simple("nama")
print("Helo nama anda siapa : {nama}".format(nama= biodata_simple["nama"]))
# biodata_simple.get("age")
print("{nama} , saya berumur : {age}".format(nama = biodata_simple.get("nama"),age = biodata_simple.get("age")))

# menambahkan key dan value 
biodata_simple["tanggal_lahir"] = "20-Sep-2000"
print("Data Setelah di update:")
print(biodata_simple)

# mengubah nilai
biodata_simple["tanggal_lahir"] = "20-09-2000"
print("Setelah di ganti format tanggal lahirnya ")
print(biodata_simple)

# menghapus nilai
del biodata_simple["tanggal_lahir"]
print("Data setelah di hapus")
print(biodata_simple)


# check key yang ada
print("List key : ")
print(biodata_simple.keys())
print("list Value : ")
print(biodata_simple.values())

