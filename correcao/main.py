import json

catalogo_livros = []

# Etapa 1 - Lero txt
with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        if linha:
            dados = linha.split(";")

            livro = {
                "id": int(dados[0]),
                "nome": dados[1],
                "descricao": dados[2],
                "preco": float(dados[3]),
                "em_estoque": int(dados[4])
            }

            catalogo_livros.append(livro)

for livro in catalogo_livros:
    print(livro)

# Etapa 2 - catalogo.json
with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)

# Etapa 3 - Adiciona 5 livros
novos_livros = [
    {
        "id": 31,
        "nome": "Python para Iniciantes",
        "descricao": "Introdução à programação com Python",
        "preco": 59.90,
        "em_estoque": 20
    },
    {
        "id": 32,
        "nome": "Java Essencial",
        "descricao": "Fundamentos da linguagem Java",
        "preco": 69.90,
        "em_estoque": 12
    },
    {
        "id": 33,
        "nome": "Banco de Dados",
        "descricao": "Conceitos de bancos de dados relacionais",
        "preco": 74.90,
        "em_estoque": 8
    },
    {
        "id": 34,
        "nome": "Arquitetura de Software",
        "descricao": "Padrões e boas práticas de arquitetura",
        "preco": 89.90,
        "em_estoque": 18
    },
    {
        "id": 35,
        "nome": "Desenvolvimento Web",
        "descricao": "Fundamentos do desenvolvimento web",
        "preco": 64.90,
        "em_estoque": 14
    }
]

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)

# Etapa 4 - Ler novamente o json
with open("catalogo.json", "r", encoding="utf-8") as arquivo:
    catalogo = json.load(arquivo)

print("\nLivros com menos de 15 unidades em estoque:")

for livro in catalogo:
    if livro["em_estoque"] < 15:
        print(
            f"ID: {livro['id']} | "
            f"Nome: {livro['nome']} | "
            f"Estoque: {livro['em_estoque']}"
        )
# Calcular valor total em estoque Loja
valor_total = 0

for livro in catalogo:
    valor_total += livro["preco"] * livro["em_estoque"]

print(f"\nValor total do estoque: R$ {valor_total:.2f}")