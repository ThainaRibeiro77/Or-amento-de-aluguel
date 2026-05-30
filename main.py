from imovel import Apartamento, Casa, Estudio
from orcamento import Orcamento


def exibir_menu_principal():
    print("\n" + "=" * 50)
    print("      BEM-VINDO À IMOBILIÁRIA R.M")
    print("=" * 50)
    print("Escolha o tipo de imóvel:")
    print("  1 - Apartamento")
    print("  2 - Casa")
    print("  3 - Estúdio")
    print("  0 - Sair")
    print("=" * 50)


def ler_inteiro(mensagem, minimo, maximo):
    """Lê e valida um número inteiro dentro de um intervalo."""
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Por favor, digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def ler_sim_nao(mensagem):
    """Lê uma resposta S ou N do usuário."""
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ("S", "N"):
            return resposta == "S"
        print("Digite S para Sim ou N para Não.")


def configurar_apartamento():
    print("\n--- APARTAMENTO ---")
    quartos = ler_inteiro("Número de quartos (1 ou 2): ", 1, 2)
    tem_crianca = ler_sim_nao("Possui crianças? (S/N): ")
    tem_garagem = ler_sim_nao("Deseja vaga de garagem? (+R$300,00) (S/N): ")
    return Apartamento(quartos, tem_crianca, tem_garagem)


def configurar_casa():
    print("\n--- CASA ---")
    quartos = ler_inteiro("Número de quartos (1 ou 2): ", 1, 2)
    tem_garagem = ler_sim_nao("Deseja vaga de garagem? (+R$300,00) (S/N): ")
    return Casa(quartos, tem_garagem)


def configurar_estudio():
    print("\n--- ESTÚDIO ---")
    print("Pacote de estacionamento: 2 vagas por R$250,00")
    print("Vagas adicionais: R$60,00 cada")
    quer_estacionamento = ler_sim_nao("Deseja incluir estacionamento? (S/N): ")

    vagas_extras = 0
    if quer_estacionamento:
        vagas_extras = ler_inteiro("Quantas vagas extras além das 2 inclusas? (0 a 10): ", 0, 10)

    # Se não quer estacionamento, vagas_extras = -1 (sinal para não cobrar)
    if not quer_estacionamento:
        vagas_extras = -1

    return Estudio(vagas_extras if quer_estacionamento else -1)


def configurar_contrato():
    print("\nContrato imobiliário: R$2.000,00 divididos em até 5 vezes")
    parcelas = ler_inteiro("Em quantas parcelas deseja pagar o contrato? (1 a 5): ", 1, 5)
    return parcelas


def main():
    print("\nIniciando sistema de orçamento...")

    while True:
        exibir_menu_principal()
        opcao = ler_inteiro("Digite sua opção: ", 0, 3)

        if opcao == 0:
            print("\nObrigado por usar o sistema da Imobiliária R.M. Até logo!")
            break

        # Cria o imóvel conforme a escolha
        if opcao == 1:
            imovel = configurar_apartamento()
        elif opcao == 2:
            imovel = configurar_casa()
        elif opcao == 3:
            imovel = configurar_estudio()

        # Configura o contrato
        parcelas = configurar_contrato()

        # Gera e exibe o orçamento
        orcamento = Orcamento(imovel, parcelas)
        orcamento.exibir_orcamento()

        # Pergunta se quer gerar CSV
        gerar = ler_sim_nao("\nDeseja gerar o arquivo CSV com as 12 parcelas? (S/N): ")
        if gerar:
            orcamento.gerar_csv()

        # Pergunta se quer fazer novo orçamento
        novo = ler_sim_nao("\nDeseja fazer um novo orçamento? (S/N): ")
        if not novo:
            print("\nObrigado por usar o sistema da Imobiliária R.M. Até logo!")
            break


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
