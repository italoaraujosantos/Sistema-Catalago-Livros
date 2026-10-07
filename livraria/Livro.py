class Livro:
    def __init__(self, id, nome, descricao, preco, qtd_estoque):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.qtd_estoque = qtd_estoque

    def lerArquivoTXT(nomeArquivo: str) -> list[Livro]:
        livros = []
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                linha = linha.strip()
                if not linha:
                    continue
                dados = linha.split(";")
                if len(dados) != 5:
                    print(f"Linha {numero_linha}: quantidade de campos inválido.")
                    continue
                try:
                    id = int(dados[0])  # id, nome, descricao, preco, e em_estoque
                    nome = str(dados[1])
                    descricao = str(dados[2])
                    preco = float(dados[3])
                    qtd_estoque = int(dados[4])
                    livro = Livro(id, nome, descricao, preco, qtd_estoque)
                    livros.append(livro)
                except ValueError:
                    print(f"Linha {numero_linha}: valor incorreto.")
        return livros

    def imprimirLeitura(livros: list[Livro]):
        for livro in livros:
            print(f"Id: {livro.id} | Nome: {livro.nome} | Descricao: {livro.descricao} | Preco: R${livro.preco:.2f} | Quantidade: {livro.qtd_estoque} \n")



