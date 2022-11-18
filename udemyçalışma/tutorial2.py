"""
class Person:#class nesne üretir,nesnenin her biri de örnek oldupundan örnek üretir
    pass

class Person():#yukardaki ile aynı şeydir
    pass

class Person(object):#yukaridakiler ile aynı şeydir
    pass
"""
"""
class nameOfClass(SuperClass):
    __init__
    __str__
    attributes(age,address,name...) #variable yerine kullanılır
    methods #function yerine kullanılır
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Eyüp",36)
p2=Person("Kadir",21)

print(p1.name, 'is', p1.age)
print(p2.name, 'is', p2.age)

p1.name="Ayşe"
print("-"*25)
p1.age=54

print(p1.name, 'is', p1.age)
print(p2.name, 'is', p2.age)

#init dediğimiz normal bir fonsiyon fakat __init__şeklinde yazılırsa fonksiyon içindekileri direkt gerçekleştiriyor,çağırmaya gerek olmuyor ve bu fonksiyona başlatıcı kurucu fonksiyon denir.
