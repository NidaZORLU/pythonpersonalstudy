class Araba():
    def __init__(self):#self yazmak zorunlu paranteze,parametredir.
        self.renk="kırmızı"
        self.yas=
        self.koltuk=5
        self="dizel"
        print("örnek oluşturuldu")
    def deneme(self):#burası çalışmaz çünkü çağrılmadı
        self.renk="mavi"
        print("burası deneme methodu")

Araba_1=Araba()
print(Araba_1.koltuk)
print(Araba_1.renk)
print(Araba_1.deneme())
Araba_1.deneme()
print(Araba_1.renk)

