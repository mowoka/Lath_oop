from BangunRuang import *

persegi = Persegi(2)
print(persegi.hitungLuas())
print(persegi.hitungKeliling())

persegiPanjang = PersegiPanjang(8, 6)
print(persegiPanjang.hitungLuas())
print(persegiPanjang.hitungKeliling())

segitiga = Segitiga(5, 8, 8)
print(segitiga.hitungLuas())
print(segitiga.hitungKeliling())

lingkaran = Lingkaran(8)
print(lingkaran.hitungLuas())
print(lingkaran.hitungKeliling())

kubus = Kubus(4)
print(kubus.hitungLuas())
print(kubus.hitungKeliling())
print(kubus.hitungVolume())