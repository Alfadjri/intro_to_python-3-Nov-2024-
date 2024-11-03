#int 
# (pagar) komentar 
x = 123456789123456789 # integer
print("ini contoh intenger : {0}".format(x))
f = 10.5 # float
print("ini contoh nilai desimal : {0} ".format(f))
z = 2 + 3j # complex
print("ini contoh tipe data kompleks : {0} ".format(z))

# Sqyence Type
a = [1,2,3] # list : nilinya harus sama dan boleh di ubah
print(a)
b = (4,5,6) # truple : nilainya tidak bisa di ubah
print(b)
c = range(0,5)  # range
print(c)

# Type text
d = "hello , word!" # string (str)

# Maping Type 
e = {"nama" : "Alfadjri Dwi Fadhilah" , "age" : 24}  # dict (dictionary) 

# Set type
f = {1,2,3} # set
g = frozenset({4,5,6}) #frozenset

# Boolean type (kondisi)
h = True; # bool (True(1), False(0));
# binary type 
i = b"Hello" #bytes
print(i)
j = bytearray(5) # bytearray
print(j)
k = memoryview(bytes(5)) # memoryview
print(k)