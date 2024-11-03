#kasus
# kita di suruh amati hewan 

class Hewan: #Hewan itu nama class
    nama_hewan = "defautl" # nama_hewan Object
    jenis_hewan = "defautl"
    umur_hewan = 10 # object property di mana umur_hewan tidak bisa di ubah private
    # def __init__(self,nama,jenis): #contruktor
    #     self.nama_hewan = nama
    #     self.jenis_hewan = jenis

    def makan(self):
        print("Hewan sedang makan !!!")


# Cara panggil 
# kucing = Hewan("tom","anggora")
kucing = Hewan()
# variabel
print("Nama kucing {nama}".format(nama = kucing.nama_hewan))
print("Jenis kucing {jenis}".format(jenis = kucing.jenis_hewan))
print("Umur hewan {umur}".format(umur = kucing.umur_hewan))
# manggil function atau method
print("Sedang apakah kucing ? ")
kucing.makan()



