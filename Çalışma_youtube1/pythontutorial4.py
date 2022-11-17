import tkinter as tk
form=tk.Tk()
form.title('Python Ders5')
form.geometry('500x400')

def topla():#aşağıda verilen toplanın işlevini belirtir.
    print('topla')

buton=tk.Button(form,text='tıkla',fg='black',bg='red',command = topla )
buton.pack(side=tk.LEFT)#butonun sola yaslanmasını sağlar
buton2=tk.Button(form,text='tıkla2',command= topla)
buton2.pack(tk.RIGHT)#butonun sağa yaslanmasını sağlar



form.mainloop()