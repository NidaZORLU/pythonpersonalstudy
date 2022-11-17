import tkinter as tk
form = tk.Tk() #tk sınıfını çağırır, form oluşturucağımız dosyanın adı, işlevi, nedir.
form.title('Tkinter Dersleri1')#açılan kutunun başlığı

etiket =tk.Label(text='Tkinter Python')
etiket.pack()#eğer girdiyi bu şekilde pack etmezsek, girdi ekranda gözükmez.
etiket2=tk.Label(form,text='Python Tkinter Dersleri')#form=konumlandırılacağı yer ve doğru kullanım nesnenin konumlandırılmasıdır.
etiket2.pack()

form.mainloop()#pencerenin açılıp, ekranda kalmasını sağlar.
