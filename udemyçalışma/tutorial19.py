class student:
    def __init__(self,name,age):
        self.name=name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

stud = student("çağrı",21)
print("name: ",stud.name,"age:",stud.get_age())
stud.set_age(25)
print("name: ",stud.name,stud.get_age())