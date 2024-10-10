import tkinter as tk

def mostrar_nomes() -> None:
    print(f"Nome: {e1.get().strip()}, Sobrenome: {e2.get().strip()}")

janela: tk.Tk = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")

tk.Label(janela, text="Nome: ").grid(row=0)
tk.Label(janela, text="Sobrenome: ").grid(row=1)

e1: tk.Entry = tk.Entry(janela)
e2: tk.Entry = tk.Entry(janela)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(janela, text="Sair", command=janela.destroy).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)

tk.mainloop()