from db import conectar

def produtos_mais_vendidos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            prod.idProduto,
            prod.descricao,
            SUM(itv.quantidade) AS quantidade_vendida,
            SUM(itv.quantidade * itv.valor) AS receita
        FROM Produto AS prod
        JOIN ItemVenda AS itv ON prod.idProduto=itv.idProduto
        GROUP BY prod.idProduto, prod.descricao
        ORDER BY receita DESC;
    """)

    print("\n=== PRODUTOS MAIS VENDIDOS ===")
    for row in cur.fetchall():
        print(f"Produto: {row[1]} | Qtde: {row[2]} | Receita: R$ {row[3]}")
    
    conn.close()


def servicos_em_execucao():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
                s.idServico,
                s.descricao,
                s.dataEntrada,
                s.dataEntrega,
                s.status
        FROM Servico AS s
        WHERE s.status = 'Em execução'
    """)

    print("\n=== SERVIÇOS EM EXECUÇÃO ===")
    for row in cur.fetchall():
        print(f"ID: {row[0]} | {row[1]} | Data Entrada: {row[2]} | Data Entrega: {row[3]} | Status: {row[4]}")
    
    conn.close()


def relatorio_servicos_completo():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            s.idServico,
            s.descricao,
            s.dataEntrada,
            s.dataEntrega,
            s.status
        FROM Servico AS s
    """)

    print("\n=== RELATÓRIO COMPLETO DE SERVIÇOS ===")
    for row in cur.fetchall():
        print(f"Serviço {row[0]} | {row[1]} | Data-Entrada {row[2]} | Data-Entrega: {row[3]} | Status: {row[4]}")

    conn.close()
