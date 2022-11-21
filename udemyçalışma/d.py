class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def show(self):
        print('Person Name: %s' %(self.name))
        print('Person Age: %s' %(self.age))
class Employe(Person):
    def __init__(self,name,age,company,sal):
        self.company=company
        self.sal=sal
        super(Employe,self).__init__(name,age)
    def __repr__(self):
        return str (self.name+self.age+self.company+self.sal)
    def showme(self):
        super(Employe,self).show()
        print('Company Name: %s'%(self.company))
        print('Employe Salary per Annum: %s' %(self.sal))
        print('\n')
    empdict={‘guido':['45',‘PYTHON','500000'],
        ‘van':['25',‘JYTHON','200000'],
        ’rossum':['35',‘ABC','400000']}
    for key,value in empdict.iteritems():
        printkey,valueemp=Employe(key,value[0],value[1],value[2])
        emp.showme()
