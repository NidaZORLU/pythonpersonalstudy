import tkinter as tk
from tkinter import font
form=tk.Tk()
form.title('Pizza Sipariş Programı')
form.geometry('500x500+400+100')

başlık=tk.Label(form,text='pizza sipariş programına hoşgeldiniz!',fg='black',bg='green',font='Times 17 italic').pack()


entry=tk.StringVar
entry1=tk.StringVar
ad_soyad=tk.Label(form,text='ad soyad:',fg='black',bg='red',font='Times 12 italic').place(x=10,y=40)
boyut=tk.Label(form,text='boyut',fg='black',bg='red',font='Times 12 italic').place(x=10,y=70)
içindekiler=tk.Label(form,text='içindekiler',fg='black',bg='red',font='Times 12 italic').place(x=10,y=100)
adres=tk.Label(form,text='adres',fg='black',bg='red',font='Times 12 italic').place(x=10,y=130)

entry_ad=tk.Entry(textvariable=entry).place(x=100,y=40)
entry_adres=tk.Entry(textvariable=entry1).place(x=100,y=130)

boyut=tk.StringVar()

radiobutton_küçük=tk.Radiobutton(form,text='Küçük boy',activebackground='blue',value='Küçük boy',variable=boyut).place(x=100,y=70)
radiobutton_orta=tk.Radiobutton(form,text='Orta boy',activebackground='blue',value='orta boy',variable=boyut).place(x=200,y=70)
radiobutton_büyük=tk.Radiobutton(form,text='Büyük boy',activebackground='blue',value='büyük boy',variable=boyut).place(x=300,y=70)

deger1=tk.StringVar()
deger2=tk.StringVar()
deger3=tk.StringVar()

check1=tk.Checkbutton(form,text='sucuklu',variable=deger1, onvalue='sucuklu').place(x=100,y=100)
check2=tk.Checkbutton(form,text='peynirli',variable=deger2, onvalue='peynirli').place(x=200,y=100)
check3=tk.Checkbutton(form,text='pastırmalı',variable=deger3, onvalue='pastırmalı').place(x=300,y=100)

def siparişver():
    bilgi=tk.Label(form, text='sipariş bilgileri',bg='yellow',font='Times 15 italic').place(x=50 ,y=240)
    ad_soyad=tk.Label(form,text='ad soyad:',fg='black',bg='red',font='Times 12 italic').place(x=10,y=270)
    boyut=tk.Label(form,text='boyut',fg='black',bg='red',font='Times 12 italic').place(x=10,y=300)
    içindekiler=tk.Label(form,text='içindekiler',fg='black',bg='red',font='Times 12 italic').place(x=10,y=330)
    adres=tk.Label(form,text='adres',fg='black',bg='red',font='Times 12 italic').place(x=10,y=360)

    ad_soyad1=tk.Label(form,text=entry.get(),fg='black',font='Times 12 italic').place(x=120,y=270)
    boyut1=tk.Label(form,text=boyut.get(),fg='black',font='Times 12 italic').place(x=120,y=300)
    içindekiler1=tk.Label(form,text=deger1.get()+' '+deger2.get()+' '+deger3.get(),fg='black',font='Times 12 italic').place(x=120,y=330)
    adres1=tk.Label(form,text=entry1.get(),fg='black',font='Times 12 italic').place(x=120,y=360)

def iptalet():
    form.quit()

sipariş=tk.Button(form,text='sipariş ver',activebackground='gray',command=siparişver).place(x=130,y=160)
iptal=tk.Button(form,text='iptal et',activebackground='gray',command=iptalet).place(x=220,y=160)

#sipariş bilgileri
bilgi=tk.Label(form, text='sipariş bilgileri',bg='yellow',font='Times 15 italic').place(x=60 ,y=240)



form.mainloop()