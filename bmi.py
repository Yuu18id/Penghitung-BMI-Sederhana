print ("##########################################")
print ("Program penghitung Berat Badan Ideal (BMI)")
print ("##########################################")
print ("Keterangan :")
print ("<18.5       = Kurus")
print ("18.5 - 22.9 = Ideal")
print ("23 - 29.9   = Gemuk")
print ("30>         = Obesitas")
print ("##########################################")

#input
berat_badan = int(input("Berat Badan (kg) :"))
tinggi_badan = float(input("Tinggi Badan (m) :"))

#process
BMI = berat_badan / tinggi_badan **2

if (BMI <= 18.5):
    keterangan = ("Kurus")
    print ("##########################################")
    print ("Perbanyak Makanan yang Bergizi ya!")
elif (BMI >=18.5 and BMI <=22.9):
    keterangan = ("Ideal")
    print ("##########################################")
    print ("Pertahankan Pola Hidup Sehatnya :)")
elif (BMI >=23 and BMI <=29.9):
    keterangan = ("Gemuk")
    print ("##########################################")
    print ("Perbanyak Olahraga dan Makanan Bergizi Ya!")
elif (BMI >=30):
    keterangan = ("Obesitas")
    print ("##########################################")
    print ("Perbanyak Olahraga dan Makanan Bergizi Ya!")

#output
print ("BMI anda bernilai", BMI, "termasuk kedalam kategori", keterangan)
print ("##########################################")
print ("Haalo")
