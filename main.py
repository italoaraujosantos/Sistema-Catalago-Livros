from livraria.Livro import Livro

if __name__ == '__main__':
    catalogo_livros = Livro.lerArquivoTXT("banco_livros.txt")
    Livro.imprimirLeitura(catalogo_livros)