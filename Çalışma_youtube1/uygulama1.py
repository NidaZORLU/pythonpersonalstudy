import tkinter as tk
form=tk.Tk()
form.title('uygulama')
form.geometry('500x300')

mail = tk.Label(text='Mail:',fg='black', bg='blue', font='Times 10 bold')
mail.place(x=10,y=30)
sıfre = tk.Label(text='şifre:',fg='black', bg='blue', font='Times 10 bold')
sıfre.place(x=10,y=60)

mail_entry=tk.Entry()
mail_entry.place(x=50,y=30)
sıfre_entry=tk.Entry(show='*')
sıfre_entry.place(x=50,y=62)

def kayıtol():
    mail = tk.Label(text='Mail:',fg='black', bg='blue', font='Times 10 bold')
    mail.place(x=10,y=150)
    sıfre = tk.Label(text='şifre:',fg='black', bg='blue', font='Times 10 bold')
    sıfre.place(x=10,y=180)
    ad = tk.Label(text='ad',fg='black', bg='blue', font='Times 10 bold')
    ad.place(x=10,y=120)

    mail_entry=tk.Entry()
    mail_entry.place(x=50,y=150)
    sıfre_entry=tk.Entry(show='*')
    sıfre_entry.place(x=10,y=180)
    ad_entry=tk.Entry()
    ad_entry.place(x=10,y=120)

def gırıs():
    mail_entry.delete(0,'end')
    sıfre_entry.delete(0,'end')
    
kayıtol_btn=tk.Button(form,text='kayıt ol',fg='black',bg='green',command=kayıtol)
kayıtol_btn.place(x=45,y=90)

gırıs_btn=tk.Button(form,text='Giriş',fg='black',bg='green',command=gırıs)
gırıs_btn.place(x=120,y=90)

form.mainloop()