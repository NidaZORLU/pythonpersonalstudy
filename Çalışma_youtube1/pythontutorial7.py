#side- left, right, top, bottom olmak üzere 4 farklı değer alır.
#fill- x ve y olmak üzere 2 değer alır.
#expand 0-1 olmak üzere iki değer alır.
#anchor n=yukarı, s=aşağı, e=sağ, w=sol, se=aşaşı sağ, sw=aşağı sol, center= orta olmak üzere 7 değer alır.

import tkinter as tk
form =tk.Tk()

label=tk.Label(text='Geometrik Yöneticiler')
label.pack(side=tk.TOP)
buton=tk.Button(text='Pack()', bg='red')
buton.pack(ipadx=20,ipady=50)#fill x ve y olmak üzre şki değer alır x olursa x boyunca büyütür. y parametresini kullanmak istersek side mutlaka vermeliyiz. (side=tk.BOTTOM, fill=tk.x, anchor='s',expand=tk.YES)
#EXPAND pencerenin boyut değişimine göre kutucuğu düzenler. ortada iste pencereyi küçütsek bile ortada kalır.
#buton.pack(padx=20,pady=100) sayfaya göre konmlar kenarlara uzaklaştırır.
#ipadx=20,ipady=100 buton boyutunu ayarlar.buton içindeki kenarlara mesafeyi arttırır.
form.mainloop()