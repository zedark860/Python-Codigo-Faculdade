def zenit_polar_replace(text: str) -> str:
    
    replacements: list[tuple[str, str]] = [
        ('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
        ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')
    ]
    
    for old, new in replacements:
        text = text.replace(old, new)
        
    return text

def main():
        
    phrase: str = "The quick brown fox jumps over the lazy dog"
    phrase = phrase.title()
    
    words: list[str] = phrase.split() # pode ser feito também com a string toda junta, pois o resultado será o mesmo
    # isso ocorre, pois o método de zenit polar substitui apenas as letras independente do contexto
    
    coded_words: list[str] = [zenit_polar_replace(word) for word in words]
    print(coded_words)
    
    coded_phrase: str = " ".join(coded_words) # aqui se fosse com letras só teria que juntar sem espaços
    
    print("Original: ", phrase)
    print("Coded: ", coded_phrase)
    
if __name__ == "__main__":
    main()