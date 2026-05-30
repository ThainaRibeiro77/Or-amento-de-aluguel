
import csv
import os
from datetime import datetime


class Orcamento:
    def __init__(self, imovel, parcelas_contrato):
        self.imovel = imovel
        self.parcelas_contrato = parcelas_contrato
        self.valor_contrato = 2000.00
        self.valor_aluguel = imovel.calcular_aluguel()
        self.valor_parcela_contrato = self.valor_contrato / parcelas_contrato

    def exibir_orcamento(self):
        valor_base   = self.imovel.valor_base
        valor_extras = self.imovel.get_valor_extras()

        print("\n" + "=" * 50)
        print("       ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M")
        print("=" * 50)
        print(self.imovel.get_resumo())
        print(f"\nValor do aluguel base:    R$ {valor_base:.2f}")
        print(f"Valor Extras:             R$ {valor_extras:.2f}")
        print(f"\nValor do contrato:        R$ {self.valor_contrato:.2f}")
        print(f"Parcelas do contrato:     {self.parcelas_contrato}x de R$ {self.valor_parcela_contrato:.2f}")
        print(f"\nTotal mensal (aluguel):   R$ {self.valor_aluguel:.2f}")
        print("=" * 50)

    def gerar_csv(self):
        # Monta nome do arquivo com data
        data_hoje = datetime.now().strftime("%d-%m-%Y")
        nome_arquivo = f"orcamento_{self.imovel.tipo.lower()}_{data_hoje}.csv"
        caminho = os.path.join(os.getcwd(), nome_arquivo)

        # utf-8-sig grava o BOM no início do arquivo, fazendo o Excel
        # reconhecer automaticamente o encoding e abrir sem caracteres quebrados
        with open(caminho, mode="w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")

            # Cabeçalho
            escritor.writerow(["Parcela", "Tipo de Imóvel", "Valor Aluguel (R$)", "Parcela Contrato (R$)", "Total Mês (R$)"])

            # 12 meses
            for mes in range(1, 13):
                # Contrato parcelado apenas nas primeiras N parcelas
                if mes <= self.parcelas_contrato:
                    parcela_contrato = round(self.valor_parcela_contrato, 2)
                else:
                    parcela_contrato = 0.00

                total_mes = round(self.valor_aluguel + parcela_contrato, 2)

                # Formata valores com vírgula como separador decimal (padrão pt-BR)
                def fmt(valor):
                    return f"{valor:.2f}".replace(".", ",")

                escritor.writerow([
                    f"Mês {mes:02d}",
                    self.imovel.tipo,
                    fmt(self.valor_aluguel),
                    fmt(parcela_contrato),
                    fmt(total_mes)
                ])

        print(f"\nArquivo CSV gerado com sucesso: {nome_arquivo}")
        return caminho
