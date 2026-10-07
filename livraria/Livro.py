import json

class Livro:
    def __init__(self, id, nome, descricao, preco, qtd_estoque):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.qtd_estoque = qtd_estoque

    def to_dict(self):
        return self.__dict__

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
            print(f"Id: {livro.id} | Nome: {livro.nome} | Descricao: {livro.descricao} | Preco: R${livro.preco:.2f} | Quantidade: {livro.qtd_estoque}")

    def gravarArquivoJSON(dados, nomeArquivo):
        # Se os dados forem uma string JSON, convertemos para objeto Python primeiro
        if isinstance(dados, str):
            dados = json.loads(dados)
        # Abre o arquivo no modo de escrita ('w') com codificação UTF-8
        with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
            # Grava os dados diretamente no arquivo de forma formatada
            json.dump(dados, arquivo, indent=4, ensure_ascii=False, sort_keys=True)

    def lerArquivoJSON(nomeArquivo: str) :
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
            livros = json.load(arquivo)
        return livros

    def imprimirLeituraJSON(livros: list[Livro]):
        for livro in livros:
            if  livro["qtd_estoque"]  > 15:
                print(f"Id: {livro['id']} | Nome: {livro['nome']} | Descricao: {livro['descricao']} | Preco: R${livro['preco']} | Quantidade: {livro['qtd_estoque']}")

