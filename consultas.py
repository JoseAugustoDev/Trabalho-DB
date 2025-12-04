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

def relatorio_especialistas_aprovacoes():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT e.idfunc, p.nome, e.especialidade,
               COUNT(s.idservico) AS servicos,
               COUNT(CASE WHEN o.status = 'Aprovado' THEN 1 END) AS aprovados,
               SUM(CASE WHEN o.status = 'Aprovado' THEN o.valor ELSE 0 END) AS valor_aprovado
        FROM especialista e
        JOIN funcionario f ON f.idfunc = e.idfunc
        JOIN pessoa p ON p.idpessoa = f.idpessoa
        LEFT JOIN atua a ON a.idespecialista = e.idfunc
        LEFT JOIN servico s ON s.idservico = a.idservico
        LEFT JOIN gera g ON g.idservico = s.idservico
        LEFT JOIN orcamento o ON o.idorcamento = g.idorcamento
        GROUP BY e.idfunc, p.nome, e.especialidade
        HAVING COUNT(o.idorcamento) > 0
        ORDER BY aprovados DESC
    """)

    dados = cur.fetchall()
    conn.close()

    print("\n=== ESPECIALISTAS QUE MAIS APROVAM ===")
    for d in dados:
        print(f"\nID: {d[0]}")
        print(f"Nome: {d[1]}")
        print(f"Especialidade: {d[2]}")
        print(f"Serviços: {d[3]}")
        print(f"Aprovados: {d[4]}")
        print(f"Valor: R$ {d[5]:.2f}")

    return dados

def relatorio_completo_servicos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT s.idservico, s.descricao, s.dataentrada, s.dataentrega,
               s.status, o.idorcamento, o.dispositivo, o.valor,
               o.status, p.nome, e.especialidade
        FROM servico s
        LEFT JOIN gera g ON g.idservico = s.idservico
        LEFT JOIN orcamento o ON o.idorcamento = g.idorcamento
        LEFT JOIN atua a ON a.idservico = s.idservico
        LEFT JOIN especialista e ON e.idfunc = a.idespecialista
        LEFT JOIN funcionario f ON f.idfunc = e.idfunc
        LEFT JOIN pessoa p ON p.idpessoa = f.idpessoa
        ORDER BY s.dataentrada DESC
    """)

    dados = cur.fetchall()
    conn.close()

    print("\n=== RELATÓRIO COMPLETO DE SERVIÇOS ===\n")
    
    for d in dados:
        print(f"{'─'*60}")
        print(f"SERVIÇO ID: {d[0]} | STATUS: {d[4]}")
        print(f"{'─'*60}")
        print(f"Descrição: {d[1]}")
        print(f"Data Entrada: {d[2]}")
        print(f"Data Entrega: {d[3] if d[3] else 'Pendente'}")
        
        if d[5]:
            print(f"\nORÇAMENTO:")
            print(f"  ID: {d[5]}")
            print(f"  Dispositivo: {d[6]}")
            print(f"  Valor: R$ {d[7]:.2f}")
            print(f"  Status: {d[8]}")
        
        if d[9]:
            print(f"\nESPECIALISTA:")
            print(f"  Nome: {d[9]}")
            print(f"  Especialidade: {d[10]}")
        
        print()

    print("=== FIM DO RELATÓRIO ===")
    
    print(f"Total de serviços: {len(dados)}")
    return dados

def relatorio_pagamentos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT formapagamento, valor, datapagamento, status
        FROM pagamento
        ORDER BY datapagamento DESC
    """)

    dados = cur.fetchall()
    conn.close()

    print("\n=== RELATÓRIO DE PAGAMENTOS ===")
    print(f"{'Forma':<15} {'Valor':<12} {'Data':<12} {'Status':<12}")
    print("─" * 60)

    total_pago = 0
    total_pendente = 0

    for d in dados:
        status = d[3] if d[3] else 'Pendente'
        print(f"{d[0]:<15} R$ {d[1]:<9.2f} {d[2]} {status:<12}")
        
        if status == 'Pago':
            total_pago += d[1]
        else:
            total_pendente += d[1]

    print("─" * 60)
    print(f"Total Pago: R$ {total_pago:.2f} | Total Pendente: R$ {total_pendente:.2f}")
    
    return dados

def orcamentos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            o.idorcamento,
            o.dispositivo,
            o.valor,
            o.status,
            p.nome AS cliente,
            e.nome AS especialista
        FROM Orcamento o
        JOIN Pessoa p ON p.idpessoa = o.idcliente
        JOIN Pessoa e ON e.idpessoa = o.idespecialista
        ORDER BY o.data;
    """)
    orcamentos = cur.fetchall()

    print("\n=== ORÇAMENTOS EXISTENTES ===")
    if not orcamentos:
        print("Nenhum orçamento cadastrado.")
    else:
        for o in orcamentos:
            print(f"ID: {o[0]} | Dispositivo: {o[1]} | Valor: R$ {o[2]:.2f} | Status: {o[3]}")

    conn.close()
    return orcamentos