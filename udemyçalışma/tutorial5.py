class Araba():
    def __init__(self,renk,km,yakit):
        self.renk=renk
        self.km=km
        self.yakit=yakit
        self.hiz=0
        self.yas=5
        self.koltuk=5
        self.calisma_durumu=False

    def calistir(self):
        self.calisma_durumu=True
    def hareket(self,yol):
        self.km+=yol
        self.yakit-=yol/20

Araba_1=Araba("kırmızı",0,50)
print(Araba_1.calisma_durumu)

Araba_1.calistir()
print(Araba_1.calisma_durumu)

Araba_1.hareket(20)
print(Araba_1.km)
print(Araba_1.yakit)