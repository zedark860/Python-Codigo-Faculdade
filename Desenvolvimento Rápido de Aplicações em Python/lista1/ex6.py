def count_search_letter(word: str, letter: str, count: int = 0) -> int:    
    if len(word) == 1:
        if word[0] == letter:
            return count + 1
        
        return count
    
    if word[0] == letter:
        count += 1
        
    return count_search_letter(word[1:], letter, count)

word: str = input("Digite uma frase: ")
word.replace(" ", "")
word.lower() 
# coloquei para ficar minúsculo, porém o próprio computador pela tabela ASCII entende minúsculo e maiusculo como diferentes
letter: str = input("Digite uma letra para ver sua quantidade: ")

print(count_search_letter(word, letter))