from db import conectar

def listar_tipos_produto():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT idTipoProduto, nomeTipo FROM TipoProduto ORDER BY idTipoProduto;")
    tipos = cur.fetchall()

    print("\n=== TIPOS DE PRODUTO EXISTENTES ===")
    if not tipos:
        print("Nenhum tipo de produto cadastrado.")
    else:
        for t in tipos:
            print(f"{t[0]} - {t[1]}")

    conn.close()
    return tipos


def inserir_tipo_produto():
    conn = conectar()
    cur = conn.cursor()

    nome = input("Digite o nome do novo tipo de produto: ")

    cur.execute("""
        INSERT INTO TipoProduto (nomeTipo)
        VALUES (%s)
        RETURNING idTipoProduto;
    """, (nome,))

    novo_id = cur.fetchone()[0]
    conn.commit()
    conn.close()

    print(f"\nTipo de produto criado com ID {novo_id}")
    return novo_id


def inserir_produto():
    print("\n=== INSERIR PRODUTO ===")

    listar_tipos_produto()

    escolha = input("\nDigite o ID do TipoProduto ou 'novo' para cadastrar um novo tipo: ")

    if escolha.lower() == "novo":
        id_tipo = inserir_tipo_produto()
    else:
        id_tipo = int(escolha)

    descricao = input("Digite a descrição do produto: ")
    quantidade = int(input("Digite a quantidade: "))

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Produto (descricao, quantidade, idTipoProduto)
        VALUES (%s, %s, %s)
        RETURNING idProduto;
    """, (descricao, quantidade, id_tipo))

    id_prod = cur.fetchone()[0]
    conn.commit()
    conn.close()

    print(f"\Produto cadastrado com ID {id_prod} e tipo {id_tipo}")


def consultar_produtos():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT idProduto, descricao, quantidade FROM Produto")
    for row in cur.fetchall():
        print(row)
    conn.close()

def atualizar_produto():
    idp = input("ID do produto a atualizar: ")
    nova_qtd = int(input("Nova quantidade: "))
    
    conn = conectar()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Produto SET quantidade=%s WHERE idProduto=%s",
        (nova_qtd, idp)
    )
    conn.commit()
    conn.close()
    print("Produto atualizado!")

def deletar_produto():
    idp = input("ID do produto a excluir: ")

    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM ItemVenda WHERE idProduto=%s;", (idp,))
        cur.execute("DELETE FROM ItemServico WHERE idProduto=%s;", (idp,))

        cur.execute("DELETE FROM Produto WHERE idProduto=%s;", (idp,))

        conn.commit()
        print("Produto e dependências excluídos!")

    except Exception as e:
        conn.rollback()
        print("Erro:", e)

    finally:
        conn.close()
