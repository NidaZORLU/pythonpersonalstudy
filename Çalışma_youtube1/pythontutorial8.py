import tkinter as tk
form=tk.Tk()
form.title('place')
form.geometry('500x450+250+250')
buton=tk.Button(form,text='deneme',fg='red',bg='green',font='Times 17 bold')
#buton.place(relx=0.5,rely=0.5)#x ve y konumunu bu şekide dinamik bir şekilde hareket ede rfakat diğer şekilde buton dinamik hareket etmemektedir.
buton.place(width=150,height=160)





form.mainloop()