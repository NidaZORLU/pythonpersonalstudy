import tkinter as tk
form =tk.Tk()
form.title('Tkinter Dersleri Formu')
label=tk.Label(form,text='Python Tkinter')
label.pack()
label2=tk.Label(form,text='Ders2',fg='red')#fg=yazı rengi
label2.pack()
label3=tk.Label(form, text='Ders2 arkaplan',fg='black',bg='green')#bg=arkaplan rengi
label3.pack()
label4=tk.Label(form,text='yeni label',fg='red',bg='blue',font='Times 15 italic')
label4.pack()
label5=tk.Label(form, text='Label',fg='black',bg='black',font='Times 17 bold')
label5.pack()
form.mainloop()