class Bisiklet():
    adet=0
    def __init__(self):
        self.fiyat=1000
        self.renk="siyah"
        self.vites=21
        Bisiklet.adet_arttır()
    @classmethod#paramtre olarak sınıfın kendisini alır static methodtan farklı olarak ve sınıfın kendisi hakkında bilgi veren decoratorlerdendir.
    #decoratorlerin görevi sınıfı ve fonksiyonu sarmak ve işlevlerini değiştirmektir.
    def adet_arttır(cls):#cls means class
        cls.adet+=1

#Bisiklet_1=Bisiklet() #bu satır eklendiğinde adet1 olurken satır silindiğinde 0 olur, bisiklet ne kadar eklersem o kadar sonuç çıkar bu satırdan 3 tane yazarsam sonuç adeti 3 cıkar
print(Bisiklet.adet)
Bisiklet.adet_arttır()#1 arttırır
print(Bisiklet.adet)

