import random
def makeDist_generate(banyak_data):
    list_data = []  
    for i in range(banyak_data):
        list_data.append(random.randint(1, 100))  
    return list_data  


def testing_loop(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1],arr[j] 


value = int(input("Banyak data yang akan di looping :"))
list_data = makeDist_generate(value)
print("Data sebelum di update :")
print(list_data)
testing_loop(list_data)
print("Data Setelah di loopig")
print(list_data)