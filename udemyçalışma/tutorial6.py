class Siparis:
    isim=""
    adet=0
    fiyat=0
    tarih=""
    firma=[]
    #print("merhaba")

#print(Siparis.adet)
Siparis.isim="ünlü holding"
Siparis.fiyat=10
Siparis.adet=10
#print(Siparis.adet)

gofret=Siparis()
kek=Siparis()
kola=Siparis()#buna örnekleme denir ve sipariş sınıfının içine dahil edilmiş olur
#print(Siparis.isim)
#print(gofret.isim)#içeriği olmassa bile çalışır

Siparis.firma.append("eti")
print(kek.firma)
#yeniden append kullanıp print yazarsak bu sefer ilk eklediğimiz firma yanına yeni eklenen firma eklenir eskisi silinmez yenisi eklenir
Siparis.firma.append("torku")
print(kek.firma)
