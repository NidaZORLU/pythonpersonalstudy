import tkinter as tk

form=tk.Tk()
form.title('Entry')
form.geometry('500x300')

entry=tk.Entry()
entry.pack()

def verial():
    etiket['text']=entry.get()#get ile entry içindeki veriler  alınır

def sil():
    entry.delete(0,'end')
    entry2.delete(0,'end')

entry2=tk.Entry(show='*')#show parametresini kullandığımızda ikinci bir kısım oluşturur ve yazarken yıldız ile kapar.
entry2.pack()

buton=tk.Button(text='sil',fg='red',bg='green',command=sil)
buton.pack()

buton=tk.Button(text='verileri al',fg='red',bg='green',command=verial)
buton.pack()

etiket=tk.Label(text='veriler burayada getirilmesi lazım')
etiket.pack()

form.mainloop()