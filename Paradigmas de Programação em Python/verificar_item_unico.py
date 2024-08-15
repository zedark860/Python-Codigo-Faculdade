class DiferentNumber():
    def __init__(self):
        self.lista_base: list = [2, 3, 7, 2, 7, 2, 7]

    def contagemItens(self) -> dict:
        contagem: dict = {}

        for numero in self.lista_base:
            if numero in contagem:
                contagem[numero] += 1
            else:
                contagem[numero] = 1
        
        return contagem
    
    def verificarNumeroUnico(self) -> int:
        dicionario_numeros: dict = self.contagemItens()

        for chave, valor in dicionario_numeros.items():
            if valor == 1:
                return chave
            
    def __str__(self) -> str:
        return f"O valor único dentro dessa lista {self.lista_base} é {self.verificarNumeroUnico()}"
    
if __name__ == "__main__":

    print(DiferentNumber())

