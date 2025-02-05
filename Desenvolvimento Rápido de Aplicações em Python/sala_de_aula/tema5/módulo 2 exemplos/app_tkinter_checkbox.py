import tkinter as tk
from tkinter import ttk

janela: tk.Tk = tk.Tk()

def escolha_carreira() -> None:
    print(f"Gerencial: {var1.get()},\nTécnica: {var2.get()}")
    
ttk.Label(janela, text="Escolha sua vocação:").grid(row=0, sticky=tk.W)

var1 = tk.IntVar()
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)

var2 = tk.IntVar()
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W)

ttk.Button(janela, text="Sair", command=janela.destroy).grid(row=3, column=0, sticky=tk.W, pady=4)
ttk.Button(janela, text="Mostrar", command=escolha_carreira).grid(row=3, column=1, sticky=tk.W, pady=4)

janela.mainloop()