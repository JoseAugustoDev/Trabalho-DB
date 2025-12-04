from crud_produto import (
    inserir_produto, consultar_produtos,
    atualizar_produto, deletar_produto
)
from consultas import (
    produtos_mais_vendidos,
    relatorio_completo_servicos,
    servicos_em_execucao,
    relatorio_pagamentos,
    relatorio_especialistas_aprovacoes,
    orcamentos
)

def menu():
    while True:
        print("\n=== MENU CONECTATECH ===")
        print("1 - Inserir produto")
        print("2 - Consultar produtos")
        print("3 - Atualizar produto")
        print("4 - Excluir produto")
        print("5 - Produtos mais vendidos")
        print("6 - Serviços em execução")
        print("7 - Relatório completo de serviços")
        print("8 - Relatório de pagamentos")
        print("9 - Relatório de especialistas e aprovações")
        print("10 - Orçamentos")

        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            inserir_produto()
        elif op == "2":
            consultar_produtos()
        elif op == "3":
            atualizar_produto()
        elif op == "4":
            deletar_produto()
        elif op == "5":
            produtos_mais_vendidos()
        elif op == "6":
            servicos_em_execucao()
        elif op == "7":
            relatorio_completo_servicos()
        elif op == "8":
            relatorio_pagamentos()
        elif op == "9":
            relatorio_especialistas_aprovacoes()
        elif op == "10":
            orcamentos()
        elif op == "0":
            print("Encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
