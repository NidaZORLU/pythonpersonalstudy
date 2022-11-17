import tkinter as tk
from PIL import Image,ImageIk
form=tk.Tk()

resim=ImageTk.PhotoImage(Image.open(Desktop/python_çalışma/resim.jpeg))

buton=tk.Button(form,image=resim).pack()


form.mainloop()