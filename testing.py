n = 19
if n % 2 == 0:
    print("n is an even number")

else:

    print("n is an odd number")

    total_umur_dalam_hari = 75
jumlah_hari_dalam_sebulan = 30

bulan = total_umur_dalam_hari / jumlah_hari_dalam_sebulan

hari = total_umur_dalam_hari / jumlah_hari_dalam_sebulan

print("Umur bayi itu sekarang " + str(bulan) + " bulan dan " + str(hari) + " hari.")

a = 9
a /= a
print(a)

a = 5
b = 3
print(a == b)

class Parrot: 
    
# instance attributes 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def sing(self,song):
        return "{} sings {}". format(self.name, song)
        
    def dance(self):
        return "{} sings now dancing".format(self.name)
    
#instance the object
blu= Parrot("Blu", 10)

#call our instance methods
print(blu.sing(""))
print(blu.dance())
