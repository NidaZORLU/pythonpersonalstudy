import tkinter as tk
form=tk.Tk()
form.geometry('500x450')

def kontrol():
    if x.get()=='1':
        print('Plain')
    elif x.get()=='2':
        print('Bold')
    elif x.get()=='3':
        print('Italic')
    elif x.get()=='4':
        print('Bold/Italic')
    else:
        print('Bold/Italic')

buton=tk.Button(form,text='"First,solve the problem.Then,write the code."-John Johnson',fg='black',bg='white',command=kontrol)
buton.pack()

x=tk.StringVar()
radio=tk.Radiobutton(form,text='Plain',activebackground='red',value='1',variable=x)
radio.pack()

radio2=tk.Radiobutton(form,text='Bold',activebackground='green',value='2',variable=x)
radio2.pack()

radio3=tk.Radiobutton(form,text='Italic',activebackground='red',value='3',variable=x)
radio3.pack()

radio4=tk.Radiobutton(form,text='Bold/Italic',activebackground='red',value='4',variable=x)
radio4.pack()



form.mainloop()