def deneme():
    "burası docstring yeri"#yorum satırı olur böylece
    """eğer ben consola deneme.__doc__ yazarsam bana çıktı olarak burası docstring yeridir çıktısını verir"""
    x=5
    y=x*2
    print(y)

class Araba():
    """bu sınıf arabaya ait nesne üretir"""#eğer ben print(Araba.__doc__)şeklinde yazarsam yorum satırında yazanın çıktısını alırım, özetlemek gerekirse print ile veya fonksiyonun ile doc stringi çağırmak demek yorum satırında yazanın çıktısını verir
    def __init__(self):#self yazmak zorunlu paranteze,parametredir.
        #bu sınıfın altındaki yorum satını merak edersem print(Araba.__init__.__doc__) şeklinde yazılarak çıktı alınabilir fakat bu fonksiyonun altında herhangi bir yorum satırı yoksa none şeklinde çıktı alınır
        self.renk="kırmızı"
        self.yas=5
        self.koltuk=5
        self="dizel"
    
    def __str__(self):
        return "burası özel açıklama yeri"#print(Araba_1 )yazarsak burası özel açıklama yeri çıktıısnı alırız
        #return "arabanın rengi:"+self.renk --- print(Araba_1) yazarsak arabanın rengi:kırmızı çıktısın alırız
Araba_1=Araba()

#class içine yazılan fonksiyonlara class ın methodu denir(sadece terim değişiyor)
#class içine yazılan değişkenlere OOPnin niteliği denir(sadece terimler değişiyior)

