a = 10
b = 5
hasil = a > b # True
print("Apakah {a} lebih besar dari (>) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
hasil = a < b # False
print("Apakah {a} lebih kecil dari (<) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
a = 2
b = 2
hasil = a >= b # True
print("Apakah {a} lebih besar sama dengan dari (>=) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
hasil = a <= b # False
print("Apakah {a} lebih kecil sama dengan dari (<=) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
hasil = a == b
print("Apakah {a} sama dengan (==) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
#tidak sama dengan (!)
a = False
hasil = a != True
print("Apakah {a} tidak sama dengan (!=) True adalah {hasil}".format(a=a,hasil=hasil))
