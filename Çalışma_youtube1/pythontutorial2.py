import tkinter as tk
form = tk.Tk()
form.title('Tkinter Dersleri ders-3')
form.geometry('500x250+500+350')#genişlikxboy+x ekseninde konumu+y ekseninde konumu
"""form.minsize(450,400)#formun inebileceği min boyut
form.maxsize(550,550)#formun çıkabileceği max boyut"""
form.resizable(False,False)#ikiside false olduğundan kullanıcı x ekseni ve y ekseni boyutunda değişiklik yapamaz. true değeri atanırsa değişikliğe izin verilmiştir. min ve max komutu ile kullanılamaz.

label=tk.Label(form,text='Ders3')
label.pack()


form.mainloop()