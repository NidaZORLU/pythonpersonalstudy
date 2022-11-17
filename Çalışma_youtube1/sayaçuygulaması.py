import tkinter as tk
sayac=0
form=tk.Tk()
form.geometry('350x300+500+150')
form.title('sayaç uygulaması')
form.config(bg='yellow')
x=tk.IntVar()

giris=tk.Entry(form,textvariable=x)
giris.place(x=60,y=50)
giris_label=tk.Label(text='giriş',bg='yellow',font='Consoles 11 bold')
giris_label.place(x=10,y=50)

def cevir():
    global sayac
    sayac=sayac+int(x.get())
    return sayac
def IleriSay():
    global sayac
    if sayac>=0:
        Sayım_label.config(text=sayac)
        sayac=sayac+1
        Sayım_label.after(200,IleriSay)
def GeriSay():
    global sayac
    if sayac>=0:
        Sayım_label.config(text=sayac)
        sayac=sayac-1
        Sayım_label.after(200,GeriSay)

buton1=tk.Button(form,text='geri say',activebackground='red',command=GeriSay)
buton1.place(x=80,y=90)
buton2=tk.Button(form,text='ileri say',activebackground='red',command=IleriSay)
buton2.place(x=130,y=90)
buton3=tk.Button(form,text='çevir',activebackground='red',command=cevir)
buton3.place(x=200,y=90)

Sayım_label=tk.Label(bg='white',font='Times 40 bold')
Sayım_label.place(x=150,y=200)

form.mainloop()