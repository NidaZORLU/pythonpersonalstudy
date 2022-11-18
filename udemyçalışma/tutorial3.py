class Araba():
    def __init__(self):#self yazmak zorunlu paranteze,parametredir.
        self.renk="kırmızı"
        self.yas=5
        self.koltuk=5
        self="dizel"
        print("örnek oluşturuldu")
    def deneme(self):#burası çalışmaz çünkü çağrılmadı
        print("burası deneme methodu")

Araba_1=Araba()
print(Araba_1.renk)

