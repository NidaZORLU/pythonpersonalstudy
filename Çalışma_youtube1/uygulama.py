import tkinter as tk
import random as rd #rastgele sayı üretmek için gerekli 

form=tk.Tk()
form.title('Tekrar Uygulaması')
form.geometry('500x400+500+350')
liste=[]
for i in range(5):
    while len(liste)!=6:
        a=rd.randint(1,50)#random şekilde belirtilen aralıktaki saayılardan döner,integer şeklinde.
        if a not in liste:
            liste.append(a)

def göster():
    label.config(text=liste)#config label özelliklerini almaya yarar, özellik değiştirilmek istenirse labeldaki gibi text yanına özellik eklenebilir ve yeni eklenen özellik aktif kullanılır.

def saydamlaştır():
    form.wm_attributes('-alpha', 0.3)

def döndür():
    form.wm_attributes('-alpha', 0.9)

def max():
    form.state('zoomed')

def min():
    form.state('iconic')

label=tk.Label(form,fg='black',bg='red',font='Times 20 bold')
label.pack()

göster=tk.Button(form,text='göster',fg='black',bg='yellow',command = göster)
göster.pack(side=tk.LEFT)
göster=tk.Button(form,text='saydamlaştır',fg='black',bg='yellow',command = saydamlaştır)
göster.pack(side=tk.LEFT)
göster=tk.Button(form,text='döndür',fg='black',bg='yellow',command = döndür)
göster.pack(side=tk.LEFT)
göster=tk.Button(form,text='max',fg='black',bg='yellow',command = max)
göster.pack(side=tk.LEFT)
göster=tk.Button(form,text='min',fg='black',bg='yellow',command = min)
göster.pack(side=tk.LEFT)

form.mainloop()
