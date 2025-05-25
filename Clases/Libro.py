class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, numero_ejemplares: int):
        self.titulo: str = titulo
        self.autor: str = autor
        self.isbn: str = isbn
        self.numero_ejemplares: int = numero_ejemplares

    def __str__(self):
        return (f"Titulo: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} -"
                f" NºEjemplares: {self.numero_ejemplares}")
