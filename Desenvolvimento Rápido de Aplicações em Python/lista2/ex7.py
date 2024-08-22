
class Author:
    def __init__(self, name: str, nacionality: str) -> None:
        self.name = name
        self.naciolationality = nacionality


class Book:
    def __init__(self, title: str, publication_year: str, author: Author) -> None:    
        self.title = title
        self.publication_year = publication_year
        self.author = author
            

class Library:
    def __init__(self, books: list[Book]) -> None:
        self.books = books
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def list_books(self) -> None:
        for book in self.books:
            print(book.title)
            
    def search_books_by_author(self, author: str):
        sorted_books = sorted(self.books, key=lambda book: book.author.name)
        
        books = [ book.title for book in sorted_books if book.author.name == author ]
        
        print(books)
        
if __name__ == "__main__":
    # fiz essa parte com ia só para testar o algoritmo, o resto do código foi feito por mim
    
    # Criando alguns autores
    author1 = Author("John", "BR")
    author2 = Author("Mary", "US")
    author3 = Author("Alice", "UK")
    author4 = Author("Bob", "CA")
    author5 = Author("Eve", "AU")

    # Criando alguns livros
    book1 = Book("Python Programming", "2022", author1)
    book2 = Book("Data Science with Python", "2021", author2)
    book3 = Book("Machine Learning Basics", "2023", author3)
    book4 = Book("Deep Learning Fundamentals", "2020", author4)
    book5 = Book("Artificial Intelligence", "2022", author5)
    book6 = Book("Advanced Python Techniques", "2023", author1)
    book7 = Book("Intro to Data Science", "2020", author2)
    book8 = Book("Python for Beginners", "2021", author3)
    book9 = Book("Neural Networks Explained", "2023", author4)
    book10 = Book("AI in Practice", "2024", author5)

    # Criando uma biblioteca e adicionando livros
    library = Library([book1, book2, book3, book4, book5])
    library.add_book(book6)
    library.add_book(book7)
    library.add_book(book8)
    library.add_book(book9)
    library.add_book(book10)

    # Listando todos os livros na biblioteca
    print("Lista de todos os livros na biblioteca:")
    library.list_books()

    # Buscando livros pelo autor "John"
    print("\nBuscando livros pelo autor 'John':")
    library.search_books_by_author("John")
    
    # Buscando livros pelo autor "Alice"
    print("\nBuscando livros pelo autor 'Alice':")
    library.search_books_by_author("Alice")
