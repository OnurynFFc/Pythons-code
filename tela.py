from tkinter import *
# janela = Tk()


# btn = Button(janela, text="olá mundo", bg='black', fg='blue')
# btn.after()
# btn.pack()

# janela.mainloop()
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=10, row=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=10)
root.mainloop()