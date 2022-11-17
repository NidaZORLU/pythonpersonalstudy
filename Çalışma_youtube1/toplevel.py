from tkinter import Tk


import tkinter as tk
form =tk.Tk()
form.geometry('250x250')
form.title('TopLevel')

toplevel=tk.Toplevel(bg='green')
toplevel.title('toplevel2')
toplevel.geometry('350x350')


toplevel.mainloop()#bunu eklemek ana pencere ile kapanmasını sağlar.
form.mainloop()