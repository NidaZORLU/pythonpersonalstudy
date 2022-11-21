class Student:
    def __init__(self,name,age):
        self.fullname=name
        self.sage=age
    def display(self):
        print ('Student FullName:%s' %(self.fullname))
        print ('Student Age: %d' %(self.sage))

s1=Student('Python',14)
s1.display()
s2=Student('jython',23)
s2.display()
s3=Student('Objects',45)
s3.display()
