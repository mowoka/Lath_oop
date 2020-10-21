class Person:

    def __init__(self, name, age, jKel):
        self.name = name
        self.age = age
        self.jKel = jKel
    
    def status(self):
        pass

class Pegawai(Person):

    def __init__(self, name, age, jKel, profesi, salary):
        super().__init__(name, age, jKel)
        self.profesi = profesi
        self.salary = salary
    
    def status(self):
        print("-------------------------------")
        print("Status data Identisa")
        print("Nama : "+self.name+"\nUmur : "+str(self.age)+"\nJenis Kelamin : "+self.jKel+"\nProfesi : "+self.profesi+"\nSalary : "+str(self.salary))



print("Input data identitas : ")
name = input("Nama : ")
umur = input("Umur : ")
j_kel = input("Jenis Kelamin : ")
profesi = input("Profesi : ")
salary = input("Gaji : ")
pegawai = Pegawai(name, umur, j_kel, profesi, salary)
pegawai.status()


