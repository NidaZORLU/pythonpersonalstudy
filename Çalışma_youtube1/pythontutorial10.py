import tkinter as tk
form=tk.Tk()
form.title('checkbutton')
form.geometry('500x500')
x=tk.IntVar
x.set(0)

def kontrol():
    if x.get()==0:
        print('onaylanmadı')
    else:
        print('onaylandı')
check=tk.Checkbutton(form,text='onay',fg='black',bg='gray',variable=x,command=kontrol)
check.pack()

form.mainloop()