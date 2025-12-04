from crud_produto import (
    inserir_produto, consultar_produtos,
    atualizar_produto, deletar_produto
)
# from consultas import (
#     produtos_mais_vendidos,
#     especialistas_aprovadores,
#     relatorio_servicos_completo,
#     servicos_em_execucao,
#     valor_por_forma_pagamento
# )

def menu():
    while True:
        print("\n=== MENU CONECTATECH ===")
        print("1 - Inserir produto")
        print("2 - Consultar produtos")
        print("3 - Atualizar produto")
        print("4 - Excluir produto")
        # print("5 - Produtos mais vendidos")
        # print("6 - Especialistas que mais aprovam orçamentos")
        # print("7 - Serviços em execução")
        # print("8 - Relatório completo de serviços")
        # print("9 - Pagamentos por forma")

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
        # elif op == "5":
        #     produtos_mais_vendidos()
        # elif op == "6":
        #     especialistas_aprovadores()
        # elif op == "7":
        #     servicos_em_execucao()
        # elif op == "8":
        #     relatorio_servicos_completo()
        # elif op == "9":
        #     valor_por_forma_pagamento()

        elif op == "0":
            print("Encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
