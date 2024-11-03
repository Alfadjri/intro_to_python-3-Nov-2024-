# kasus
# Manusia

class Ibu:
    panggilan = "default"
    # def __init__(self,panggilan): #contruktor ini harus di isi saat di panggil 
    #     self.panggilan = panggilan
    
    def memanggil(self):
        print("Iya, Ada Apa ?")

    #Enkapsulasi mode  
    def setSifat(self,sifat):
        self.__sifat = sifat
    def getSifat(self):
        return self.__sifat
    

class Anak(Ibu):
    def suruh(self):
        print("Nati dulu lah !!!!")

sekolah = Anak()

print("Siapa nama anak ini : {nama_anak}".format(nama_anak = sekolah.panggilan))
sekolah.memanggil()