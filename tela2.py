import tkinter as tk

# janela = tk.Tk()
# janela.title('Teste de janela')

# #Rótulo
# rotulo = tk.Label(janela, text='Olá, mundo')
# rotulo.pack()


# janela.mainloop()

#função para exibir 
def exibir():
    print('Foi cliclado')

def calc():
    n1 = int()
    n2 = int()
    print(n1+n2)

janela = tk.Tk()
janela.geometry('500x500')
janela.title('Botão')

btn1 = tk.Button(janela, text='Clique aqui', border='3', background='black', width='20', height='20',command=exibir)
btn2 = tk.Button(janela, text='apague', border='3', background='red', width='20', height='20', command=calc)

entrada1 = tk.Entry()
entrada2 = tk.Entry()


entrada1.place(x=30 , y=30)
entrada2.place(x=30 , y=90)




btn1.pack()
btn2.pack()

janela.mainloop()