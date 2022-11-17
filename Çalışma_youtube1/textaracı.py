import tkinter as tk
form=tk.Tk()
form.geometry('400x400')
form.title('text_aracı')
form.config(bg='yellow')

text=tk.Text(form,width=20,height=20,padx=10,pady=10,bd=5,selectbackground='green',font='consoles 17 italic').pack()#bd=çerçeve ekler,padx,y=yazı içinde kenarlara boşluk bırakır.selecktbackground=seçilen yerin rengini belirler.




form.mainloop()