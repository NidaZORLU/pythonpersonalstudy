import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import tcdogrulama

form=tk.Tk()
form.geometry('300x300')
form.config(bg='black')
form.title('Arıza Bildirim Uygulaması')

label_baslık=tk.Label(form,text='Arıza Bildirim Uygulaması',bg='black',fg='white',font='times 17 bold')
label_baslık.pack()


label_ad=tk.Label(form,text='Kullanıcı Adı',bg='black',fg='white',font='Times 12 bold')
label_ad.place(x=20,y=90)

label_sıfre=tk.Label(form,text='Şifre',bg='black',fg='white',font='Times 12 bold')
label_sıfre.place(x=20,y=110)

entry_ad=tk.Entry(form)
entry_sıfre=tk.Entry(form,show='*')
entry_ad.place(x=120,y=95)
entry_sıfre.place(x=120,y=135)

def giris():
    if entry_ad.get()=='nidazorlunz' and entry_sıfre=='1234.4321.':
        msg=messagebox.showinfo('tebrikler', message='giriş başarılı')
        if msg=='ok':
            basvuru_formu=tk.Toplevel()
            basvuru_formu.geometry('350x350')
            basvuru_formu.title('arıza bildirim formu')
            basvuru_formu.config(bg='yellow')
            baslık_label=tk.Label(basvuru_formu,text='Arıza bildirim formu',bg='yellow',fg='red',font='Times 20 bold')
            baslık_label.pack()
            label_ad=tk.Label(basvuru_formu,text='Ad-Soyad:',font='consoles 12 italic',bg='yellow',fg='black').place(x=40,y=50)
            label_ad=tk.Label(basvuru_formu,text='Tc no:',font='consoles 12 italic',bg='yellow',fg='black').place(x=40,y=90)
            label_ad=tk.Label(basvuru_formu,text='Modem tipi:',font='consoles 12 italic',bg='yellow',fg='black').place(x=40,y=130)
            label_ad=tk.Label(basvuru_formu,text='Arıza tipi:',font='consoles 12 italic',bg='yellow',fg='black').place(x=40,y=170)
            label_ad=tk.Label(basvuru_formu,text='Adres :',font='consoles 12 italic',bg='yellow',fg='black').place(x=40,y=210)
            label_ad=tk.Label(basvuru_formu,text='Mail:',font='consoles 12 italic',bg='yellow',fg='black').place(x=40,y=250)

            entry_ad_soyad=tk.Entry(basvuru_formu)
            entry_ad_soyad.place(x=140,y=50)

            entry_tc_no=tk.Entry(basvuru_formu)
            entry_tc_no.place(x=140,y=90)

            liste=['Tmp', 'KMNR', '2TMNx', 'MTPL', 'NMPY', 'PNDAS']
            combo_modem=Combobox(basvuru_formu,values=liste).place(x=140,y=130)

            liste1=['kablo','giriş arızalı','wifi açılmıyor', 'internet çekmiyor', 'nmpy', 'pndas']
            combo_modem=Combobox(basvuru_formu,values=liste1).place(x=140, y=170)

            entry_adres=tk.Entry(basvuru_formu)
            entry_adres.place(x=140,y=210)

            entry_mail=tk.Entry(basvuru_formu)
            entry_mail.place(x=140,y=250)

            def olustur():
                kosul=tc_doğrulama.Tc(entry_tc_no.get())

                if kosul==True:
                    msgm=messagebox.showinfo('basarıyla oluştu',message='arıza bildirimi gerçekleştirildi.')
                else:
                    messagebox.showerror('Başarısız','tc kimlik numaranızı doğru girdiğinize emin olunuz.')

            buton=tk.Button(basvuru_formu,text='oluştur',command=olustur).place(x=140,y=290)
            
            basvuru_formu.mainloop()

def iptal():
    pass

buton_giris=tk.Button(form, text='Giriş',activebackground='green',command=giris)
buton_iptal=tk.Button(form,text='iptal',activebackground='red',comman=iptal)
buton_giris.place(x=120,y=180,width=60)
buton_iptal.place(x=190,y=180,width=60)

form.mainloop()