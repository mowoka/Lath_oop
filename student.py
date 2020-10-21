class Student:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setEmail(self, email):
        self.email = email
    
    def getName(self, name):
        return self.name
    
    def getAge(self, age):
        return self.age
    
    def getName(self, email):
        return self.email
    
    def status(self):
        print("-------------------------------")
        print("Status data Identitas")
        print("Nama : "+self.name+"\nUmur : "+str(self.age)+"\nEmail : "+self.email)

class pythonSwitch:

    def swicth(self, arg):
        default = "Silahkan pilih sesuai nomor yang diberikan"
        return getattr(self, 'case_' + str(arg), lambda: default)()
    
    def case_1(self):
        name = input("Nama : ")
        student.setName(name)
        age = input("Age : ")
        student.setAge(age)
        email = input("Email : ")
        student.setEmail(email)

    def case_2(self):
        student.status()

    def case_3(self):
        for i in pengumuman_2:
            print(i)
        
        arg = input("Pilihan : ")
        if arg == "1":
            ename = input("Enter Name : ")
            student.setName(ename)
        elif arg == "2":
            eumur = input("Enter Age : ")
            student.setAge(eumur)
        elif arg == "3":
            eemail = input("Enter Umur : ")
            student.setEmail(eemail)
        

# Varianbel
name = "-"
age = 0
email = "-"
student = Student(name, age, email)
s = pythonSwitch()
pengumuman_1 = ["----------------------------",
              "Sistem Informasi Identitas",      
              "1. isi data identias",
              "2. lihat data identias",
              "3. edit data identias",
              "4. Exit",
                ]

pengumuman_2 =  [
                 "---------------------------",
                 "1. Edit Nama ",
                 "2. Edit Umur",
                 "3. Edit Email",
                ]

while True:    
    for i in pengumuman_1:
        print(i)
    print("")
    p_input = input("Siahkan pilih : ")
    if p_input.lower() == "exit" or p_input == "4":
        break 
    s.swicth(p_input)
    print("----------------------------")

print("Good bye")