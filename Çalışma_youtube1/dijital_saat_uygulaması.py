import tkinter as tk
import time
form=tk.Tk()
form.title('Dijital Saat Uygulaması')
form.geometry('250x200+250+250')
form.config(bg='yellow')

def zaman():
    zaman_formatı=time.strftime('%H:%M:%S')#zamanı hangi formatta istediğimiz bilgisini veririz.
    zaman_label.config(text=zaman_formatı)
    zaman_label.after(200,zaman())#ne kadar sürede bir yenilenmesini istediğimizi belirtiriz bu kısımda.200milisaniyede 1 çalışır.5000 olursa fonksiyon 5sn bir değişir 19 iken bir anda 24 olur.

zaman_label=tk.Label(bg='white',font='Times 35 bold')
zaman_label.place(x=30,y=80)
zaman()

baslık=tk.Label(text='Dijital Saat Uygulaması',font='Times 15 bold',bg='yellow').pack()
baslık1=tk.Label(text='TKinter Dersleri 21',font='Times 15 bold',bg='yellow').pack(side=tk.BOTTOM)



form.mainloop()