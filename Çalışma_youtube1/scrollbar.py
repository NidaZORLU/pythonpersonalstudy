import tkinter as tk
form=tk.Tk()

scrol=tk.Scrollbar()
scrol.pack(side=tk.RIGHT,fill=tk.Y)

Listebox=tk.Listbox(form,yscrollcommand=scrol.get())

for i in range(500):
    Listebox.insert('end','TKinter dersleri'+str(i))#eleman ekleme

Listebox.pack(side=tk.LEFT)

scrol.config(command=Listebox.yview)


form.mainloop()