import math

class PersegiPanjang:

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self):
        return self.panjang * self.lebar
    
    def hitungKeliling(self):
        return 2*(self.panjang + self.lebar)

class Persegi:

    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi * self.sisi
    
    def hitungKeliling(self):
        return 4 * self.sisi

class Segitiga:

    def __init__(self, alas, tinggi, digonal):
        self.alas = alas
        self.tinggi = tinggi
        self.diagonal = digonal
    
    def hitungLuas(self):
        return 0.5 * self.alas * self.tinggi
    
    def hitungKeliling(self):
        return self.alas + self.tinggi + self.diagonal

class Lingkaran:

    def __init__(self, jari):
        self.jari = jari

    def hitungLuas(self):
        return math.pow(self.jari, 2) * 3.14

    def hitungKeliling(self):
        return 2 * 3.14 * self.jari

class Kubus:
    
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitungLuas(self):
        return 6 * math.pow(self.sisi, 2)
    
    def hitungKeliling(self):
        return 12 * self.sisi
    
    def hitungVolume(self):
        return math.pow(self.sisi, 3)

class Balok:

    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitungLuas(self):
        return 2 * ((self.panjang * self.lebar) + (self.panjang * self.tinggi) + (self.lebar * self.tinggi))

    def hitungKeliling(self):
        return 4 * (self.panjang + self.lebar + self.tinggi)
    
    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

class LimasPersegi:

    def __init__(self, p_alas, p_tegak, t_limas, t_segitiga):
        self.p_alas = p_alas
        self.p_tegak = p_tegak
        self.t_limas = t_limas
        self.t_segitiga = t_segitiga
    
    def hitungLuasPermukaan(self):
        return math.pow(self.p_alas, 2) + 4 * (0.5 * self.p_alas * self.t_segitiga)
    
    def hitungPanjangKerangka(self):
        return (4 * self.p_alas) + (4 * self.p_tegak)
    
    def hitungVolume(self):
        return math.pow(self.p_alas, 2) * self.t_limas / 3
    