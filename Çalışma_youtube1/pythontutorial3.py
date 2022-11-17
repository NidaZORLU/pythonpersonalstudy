import tkinter as tk
form=tk.Tk()
form.title('Python dersleri')
form.geometry('500x500+350+250')
form.state('normal')
#form.state('zoomed')#normal=normal boyutta çıkarır, zoomed=tam ekran çıkarır.istenilen boyutta pencere oluşturmaya yarar.
#form.state('iconic')#gözükmicek şekilde altta açılır, bu şeklde pencerenin 3 durumu mevcuttur.
form.wm_attributes('-alpha, 0.3')#değer 0-1 arası verilebilir.pencerenin saydamlığı için kullanılan bir komuttur.

form.mainloop()