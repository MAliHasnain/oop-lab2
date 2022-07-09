class Student:
    def __init__(self,name,batch,year):
        self.name=name
        self.batch=batch
        self.year=year

A=Student("ALI HASNAIN","2021","2022")
B=Student("ABBAS RAZA","2021","2022")
C= Student("JARI NAQVI","2018","2022")
print(A.name)
print(B.batch)
print(C.year)