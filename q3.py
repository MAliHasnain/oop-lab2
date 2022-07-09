class Student:
    def __init__(self,name="ALI HASNAIN",batch="2021"):
        self.name=name
        self.batch=batch
    def __init__(self,department="CIS"):
        self.department=department
A1=Student()
print(A1.department)

## In a single class there could not be more than one constructor.#
## If we apply more than one constructor than the last constructor overwrites the previous one!!!#