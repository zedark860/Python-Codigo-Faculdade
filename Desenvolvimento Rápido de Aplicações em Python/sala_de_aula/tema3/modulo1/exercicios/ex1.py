list_text: list[str] = []

while True:
    text_user: str = input("Escreva algo: ").strip()
    
    list_text.append(text_user)
    
    input_option: str = input("Deseja continuar? [S/N] ")
    
    if input_option.upper() == "N":
        break
    
with open("meu_arquivo.txt", "w") as file:
    for text in list_text:
        file.write(f"{text.upper()}\n")