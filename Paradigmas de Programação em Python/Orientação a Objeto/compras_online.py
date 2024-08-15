
#Crie um sistema para automatizar compras online. A priori, esse programa precisa ter duas classes: uma para definir as características e métodos do produto e outra para definir as características e métodos da compra.
#Esse programa deverá ser capaz de adicionar produtos, remover produtos, adicionar desconto ao valor e retornar a soma total.

class CarrinhoProdutos:
    def __init__(self, nome_produto=None, preco_produto=None):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto

class UtilidadesCarrinho:
    def __init__(self):
        self.lista_compras = []
    
    def adicionar(self, produto):
        self.lista_compras.append(produto)
        print(f"Produto {produto.nome_produto} adicionado a lista!")

    def remover(self, nome_produto):
        if not self.lista_compras:
            print("A lista de produtos ainda não tem nada! Adicione um produto") 
            return False

        for produto in self.lista_compras:
            if produto.nome_produto == nome_produto:
                self.lista_compras.remove(produto)
                print(f"Produto removido {produto} da lista!")
                return True
        print(f"Produto {produto.nome_produto} não encontrado na lista!")
        return False
    
    def listar(self):
        if not self.lista_compras:
            print("A lista de produtos ainda não tem nada! Adicione um produto") 
            return

        for produto in self.lista_compras:
            print(f"Nome produto: {produto.nome_produto}, Preço: {produto.preco_produto}")

    def desconto(self, valor_desconto):
        if not self.lista_compras:
            print("A lista de produtos ainda não tem nada! Adicione um produto para aplicar desconto") 
            return

        for produto in self.lista_compras:
            produto.preco_produto -= valor_desconto

    def total(self):
        total = 0

        if not self.lista_compras:
            print(f"O total é igual a {total}, pois a lista ainda está vazia") 
            return

        for produto in self.lista_compras:
            total += produto.preco_produto
        print(f"Preço total é {total}")

if __name__ == "__main__":
    lista_de_compras  = UtilidadesCarrinho()

    while True:
        print("""
              1: Adicionar
              2: Remover
              3: Listar
              4: Aplicar desconto
              5: Preço total no momento
              0: Finalizar
              """)
        
        try:
            opcao = int(input("Digite a opção que deseja utilizar: "))

            match opcao:
                case 1:
                    produto = input("Digite o nome do produto: ").strip().lower()
                    preco = float(input("Digite o valor do produto: "))
                    lista_de_compras.adicionar(CarrinhoProdutos(produto, preco))

                case 2:
                    produto = input("Digite o nome do produto: ").strip().lower()
                    lista_de_compras.remover(CarrinhoProdutos(nome_produto=produto))

                case 3:
                    lista_de_compras.listar()

                case 4:
                    desconto = float(input("Digite o valor do desconto a ser aplicado: "))
                    lista_de_compras.desconto(desconto)

                case 5:
                    lista_de_compras.total()

                case 0:
                    lista_de_compras.total()
                    lista_de_compras.listar()
                    print("Volte sempre!")
                    break

                case _:
                    print("Você não escolheu nenhuma das opções, tente novamente!")
                    continue
        except ValueError as e:
            print(f"Por favor, digite um valor numérico! {e}")
        except Exception as e:
            print(f"Algo deu errado {e}!")
        
