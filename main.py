from livraria.Livro import Livro

if __name__ == '__main__':
    ## Leitura arquivo txt criando lista de objetos Livros
    catalogo_livros = Livro.lerArquivoTXT("banco_livros.txt")
    Livro.imprimirLeitura(catalogo_livros)

    #Gravar dados em json
    catalogo_livros_to_dict = [livro.to_dict() for livro in catalogo_livros]
    Livro.gravarArquivoJSON(catalogo_livros_to_dict, "catalogo.json")

    #Ler arquivo json
    catalogoJSON = Livro.lerArquivoJSON("catalogo.json")
    Livro.imprimirLeituraJSON(catalogoJSON)