class Company:
    def __init__(self):
        self.__project="nlp"

class Employee(Company):
    def __init__(self,name):
        self.name=name
        Company.__init__(self)

    def show(self):
        print("Employee name: ", self.name)
        #print("working on project:",self.__project)

c=Employee("jessa")
c.show()
#print('project:', c.__project)
print('salary: ', c._Company__project)


