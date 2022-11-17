import tkinter as tk
from tkinter import messagebox

form=tk.Tk()
form.geometry('500x500')
form.title('Messagebox')

def message():
    messagebox.showinfo(title='mesaj1',message='lütfen mesaja riayet edelim!')
    messagebox.askretrycancel(title='mesaj2',message='lütfen et artık!')
    messagebox.askyesno(title='mesaj3',message='artık')
    messagebox.askquestion(title='mesaj4',message='son')


buton=tk.Button(form,text='tıkla mesaj gelsin',command=message).pack()



form.mainloop()