class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary =salary


emp=Employee('Jessa',10000)
print('name:', emp.name)
print('salary: ', emp._Employee__salary)
