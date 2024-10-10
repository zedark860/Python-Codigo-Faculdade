import tkinter as tk

janela = tk.Tk()

v = tk.IntVar()

tk.Label(janela,text="""Escolha uma linguagem de programação:""",justify = tk.LEFT, padx = 20).pack()

tk.Radiobutton(janela, text="Python", padx = 20, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="Java", padx = 20, variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx = 20, variable=v, value=3).pack(anchor=tk.W)

tk.mainloop()