import tkinter as tk
form=tk.Tk()
form.title('spinbox')
form.config(bg='pink')#sayfa arka planı değişikliği
form.geometry('400x400')

x=tk.IntVar()#diğer yönteme gerekli
y=tk.IntVar()#diğer yönteme gerekli

spin=tk.Spinbox(form,from_=10,to=100, textvariable=x).pack()#textvariable diğer yönteme gerekli
spin2=tk.Spinbox(form,from_=10,to=20,textvariable=y).pack()

def verial():
    #spin.get() normal kullanım bu şekildedir fakat çalışmazsa diğer yöntemi kullanınız.
    print(x.get())
    print(y.get())
    
buton=tk.Button(form,text='verial',command=verial).pack



form.mainloop()