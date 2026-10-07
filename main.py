from livraria.Livro import Livro
import json

if __name__ == '__main__':
    ## Leitura arquivo txt criando lista de objetos Livros
    catalogo_livros = Livro.lerArquivoTXT("banco_livros.txt")
    Livro.imprimirLeitura(catalogo_livros)

    #Gravar dados em json
    Livro.gravarArquivoJSON(catalogo_livros.Livro.to_dict(), "catalogo.json")