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
    def __init__(self):
        self.name="Mustafa"
        self.age=23
    def deneme(self):
        pass
#init dediğimiz normal bir fonsiyon fakat __init__şeklinde yazılırsa fonksiyon içindekileri direkt gerçekleştiriyor,çağırmaya gerek olmuyor ve bu fonksiyona başlatıcı kurucu fonksiyon denir.
