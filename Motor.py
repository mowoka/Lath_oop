class Motor:

    def __init__(self, merek, warna, type, cc):
        self.merek = merek
        self.warna = warna
        self.type = type
        self.cc = cc
    
    def setMerek(self, merek):
        self.merek = merek

    def setWarna(self, warna):
        self.warna = warna

    def setType(self, type):
        self.type = type

    def setCc(self, cc):
        self.cc = cc
    
    def getMerek(self):
        return self.merek
    
    def getWarna(self):
        return self.warna

    def getType(self):
        return self.type

    def getCc(self):
        return self.cc

class MengendaraiMotor(Motor):

    def __init__(self, merek, warna, type, cc, nama, noKend, modelMesin):
        super().__init__(merek, warna, type, cc)
        self.nama = nama
        self.noKend = noKend
        self.modelMesin = modelMesin
        self.mengendarai = False
        self.kecepatan = 0


    def setNama(self, nama):
        self.nama = nama

    def setNoKend(self, noKend):
        self.noKend = noKend

    def setModelMesin(self, modelMesin):
        self.modelMesin = modelMesin

    def getNama(self):
        return self.nama

    def getNoKend(self):
        return self.noKend

    def getModelMesin(self):
        return self.modelMesin

    def naikMotor(self):
        self.mengendarai = True

    def parkirMotor(self):
        self.mengendarai = False

    def tambahKecepatan(self):
        if self.mengendarai == True:
            self.kecepatan += 5
        else:
            print("Anda belum menaiki kendaraan")
        
    def kurangiKecepatan(self):
        if self.kecepatan != 0:
            self.kecepatan -= 2
        else:
            print("Kecepatan sudah 0")

    def cekKecepatan(self):
        return self.kecepatan

    def statusNaikMotor(self):
        return self.mengendarai

    def listData(self):
        print("Merek Kendaraan : "+self.merek+"\nWarna Kendaraan : "+self.warna+"\nType Kendaraan : "+self.type+"\nCC Kendaraan : "+str(self.cc)+"\nNama Pemilik : "+self.nama+"\nNomor Kendaraan : "+str(self.noKend)+"\nModel Mesin : "+self.modelMesin)
