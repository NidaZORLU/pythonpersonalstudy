#class inheritance(kalıtım,gen,miras,soyaçekim..)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print('happy birthday you were',self.age)
        self.age+=1
        print('you are now',self.age)
    
    def is_teenager(self):
        return self.age < 20 
    
Mustafa=Person("MUSTAFA",23)
print(Mustafa)
Mustafa.birthday()
print(Mustafa.is_teenager())

class Employee(Person):#person yazdığımız zaman yukardaki person sınıfındaki her sey aynı zamanda bu sınıfın niteliği olur
    def __init__(self,name,age,id):#yukardakinden miras aldığımız için aynı özelliklere dahip olmalı fakat id gibi ekstra ekleyebiliriz
        super().__init__(name,age)#init fonksiyonuna git ve age götür beni
        self.id=id

    def calculate_pay(self,hours_worked):
        rate_of_pay=7.5
        if self.age>=21:
            rate_of_pay += 2.5
        return hours_worked * rate_of_pay


    



