import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random
import string

def armazenar_parametros():
    palavras = ["python", "programação", "computador", "jogo", "aplicativo", "desenvolvimento", "inteligência", "artificial"]
    palavra_chave = random.choice(palavras)
    return palavra_chave

def verificar_letra(letra_chute, palavra_chave, letras_corretas, letras_incorretas, label_status, label_dica, label_letras_escolhidas):
    global tentativas

    if not letra_chute:
        label_status.configure(text="Digite uma letra válida.")
        return

    if letra_chute in letras_corretas or letra_chute in letras_incorretas:
        label_status.configure(text=f"A letra {letra_chute} já foi escolhida.")
        return

    if tentativas == 4:
        label_dica.configure(text=f"Dica: A palavra começa com a letra '{palavra_chave[0]}'.")
    
    if tentativas == 0:
        label_dica.configure(text=f"Dica: A última letra da palavra é '{palavra_chave[-1]}'.")

    tentativas -= 1

    if letra_chute == palavra_chave:
        label_status.configure(text=f"Parabéns! Você acertou a palavra-chave: {palavra_chave}")
        if messagebox.askyesno("Jogo da Forca", "Você ganhou! Deseja jogar novamente?"):
            reiniciar_jogo(label_letras_escolhidas, label_dica)
        return

    if letra_chute in palavra_chave:
        letras_corretas.append(letra_chute)
        label_status.configure(text=f"A letra {letra_chute} está na palavra-chave.")
        if set(letras_corretas) == set(palavra_chave):
            label_status.configure(text=f"Parabéns! Você acertou a palavra-chave: {''.join(palavra_chave)}")
            if messagebox.askyesno("Jogo da Forca", "Você ganhou! Deseja jogar novamente?"):
                reiniciar_jogo(label_letras_escolhidas, label_dica)
            else:
                messagebox.showinfo("Jogo da Forca", "O programa será encerrado.")
                root.quit()
            return
    else:
        letras_incorretas.append(letra_chute)
        if tentativas > 0:
            label_status.configure(text=f"Você errou. Letras incorretas: {' '.join(letras_incorretas)} | Tentativas restantes: {tentativas}")
        else:
            label_status.configure(text=f"Você perdeu! A palavra-chave era: {''.join(palavra_chave)}")
            if messagebox.askyesno("Jogo da Forca", "Deseja jogar novamente?"):
                reiniciar_jogo(label_letras_escolhidas, label_dica)
            else:
                messagebox.showinfo("Jogo da Forca", "O programa será encerrado.")
                root.quit()
            return

    letras_escolhidas = f"Letras escolhidas: {' '.join(letras_corretas + letras_incorretas)}"
    label_letras_escolhidas.configure(text=letras_escolhidas)

    palavra_revelada = ''.join([letra if letra in letras_corretas else '_' for letra in palavra_chave])
    label_palavra_chave.configure(text=palavra_revelada)

def on_click():
    letra_chute = entry.get().lower()
    entry.delete(0, tk.END)
    verificar_letra(letra_chute, palavra_chave, letras_corretas, letras_incorretas, label_status, label_dica, label_letras_escolhidas)

    if not letra_chute:
        button.configure(state=tk.DISABLED)

def reiniciar_jogo(label_letras_escolhidas, label_dica):
    global letras_corretas, letras_incorretas, tentativas
    letras_corretas = []
    letras_incorretas = []
    tentativas = 6
    label_status.configure(text="Digite uma letra:")
    button.configure(state=tk.NORMAL)
    label_letras_escolhidas.configure(text="")
    label_palavra_chave.configure(text="")
    label_dica.configure(text="")

def validar_entrada(event):
    if event.char not in string.ascii_letters and event.char != '\b':
        return "break"

def habilitar_botao(event):
    if entry.get():
        button.configure(state=tk.NORMAL)
    else:
        button.configure(state=tk.DISABLED)

if __name__ == "__main__":
    palavra_chave = armazenar_parametros()
    letras_corretas = []
    letras_incorretas = []
    tentativas = 5

    root = ctk.CTk()
    root.title("Jogo da Forca")

    label_palavra_chave = ctk.CTkLabel(root, text="")
    label_palavra_chave.pack(pady=10)

    label = ctk.CTkLabel(root, text="Digite uma letra no campo para começar:")
    label.pack(pady=10)

    entry = ctk.CTkEntry(root)
    entry.pack(pady=10)

    button = ctk.CTkButton(root, text="Chutar", command=on_click)
    button.pack(pady=10)

    label_status = ctk.CTkLabel(root, text="")
    label_status.pack(pady=10)
    
    label_letras_escolhidas = ctk.CTkLabel(root, text="")
    label_letras_escolhidas.pack(pady=10)

    label_dica = ctk.CTkLabel(root, text="")
    label_dica.pack(pady=10)

    button.configure(state=tk.DISABLED)
    entry.bind("<KeyRelease>", habilitar_botao)
    entry.bind("<Key>", validar_entrada)

    largura_janela = 400
    altura_janela = 400
    posicao_x = (root.winfo_screenwidth() // 2) - (largura_janela // 2)
    posicao_y = (root.winfo_screenheight() // 2) - (altura_janela // 2)
    root.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

    root.mainloop()
