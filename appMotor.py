from Motor import *


# Variabel 
bekendara = [
    "1. Tambah Kecepatan",
    "2. Kurangi kecepatan",
    "3. Turun dari kendaraan"
]
# ---------------------------------------------------------
print("------------------------------")
print("--------Isi data Awal---------")
# Variable dumy
merek = "honda"
warna = "hitam"
type = "bebek"
cc = 125
nama = "Giofanny Mowoka"
noKend = 5551555
modelMesin = "Gigi"

# merek = input("Merek Kendaraan : ")
# warna = input("Warna Kendaraan : ")
# type = input("Type Kendaraan : ")
# cc = input("CC Kendaraan : ")
# nama = input("nama Pemilik Kendaraan : ")
# noKend = input("Nomor Kendaraan Kendaraan : ")
# modelMesin = input("Model mesin Kendaraan : ")

mengendarai = MengendaraiMotor(merek, warna, type, cc, nama, noKend, modelMesin)  
mengendarai.listData()
print(mengendarai.statusNaikMotor())
tanya = input("Apakah anda ingin menaiki kendaraan ? Ya / tidak ")
if tanya.lower() == "ya":
    print("Mengendarai")
    mengendarai.naikMotor()
    
    while mengendarai.statusNaikMotor != False:
        print("Anda Sedang Mengendarai motor")
        print(mengendarai.statusNaikMotor())
        for i in bekendara:
            print(i)
        pilihan = input("Pilih : ")
        if pilihan == "1":
            mengendarai.tambahKecepatan()
            print(mengendarai.cekKecepatan())
        elif pilihan == "2":
            mengendarai.kurangiKecepatan()
            print(mengendarai.cekKecepatan())
        elif pilihan == "3":
            if mengendarai.cekKecepatan() == 0:
                mengendarai.parkirMotor()
                if mengendarai.statusNaikMotor() == False:
                    break
        else:
            print("Silahkan untuk mengurangi kecepatan sampai 0")
            print(mengendarai.cekKecepatan())

else:
    print("Harap di standar lagi")


print("Selamat anda selesai dalam latihan mengendarai Motor")