import tkinter as tk
from tkinter.ttk import Combobox
form=tk.Tk()
form.geometry('450x450')
x=tk.StringVar

Python=['NumPy','pandas','Matplot','seaborn','TKinter']
kutu=Combobox(form,values=Python,height=3, textvariable=x).pack()#bu şekildede açılır kutuya değer atanabilir.#height ekranda gösterilecek miktar
#kutu=Combobox(form,values=('1','2','3')).pack()#bu şekilde açılır kutuya değer atanablilir.
def yazdır():
    print(x.get())
    
buton=tk.Button(form, text='yazdır',command=yazdır).pack()





form.mainloop()