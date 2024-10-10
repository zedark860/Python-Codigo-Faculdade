import tkinter as tk
from tkinter import messagebox as mb


def resposta() -> None:
    mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")
    
def verificacao() -> None:
    if not mb.askyesno("Verificar", "Realmente quer sair?"):
        mb.showinfo('No', 'A opção de Sair foi cancelada')
        return
        
    mb.showwarning('Yes', 'Ainda não foi implementado')
    
tk.Button(text="Sair", command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)

tk.mainloop()