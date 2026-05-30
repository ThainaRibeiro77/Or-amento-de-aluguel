
class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo
        self.valor_base = 0
        self.valor_garagem = 0
        self.valor_contrato = 2000.00

    def calcular_aluguel(self):
        return self.valor_base

    def adicionar_garagem(self):
        self.valor_garagem = 300.00

    def get_valor_extras(self):
        # Retorna o total de extras (garagem, estacionamento, etc.)
        # Subclasses sobrescrevem se tiverem mais tipos de extra
        return self.valor_garagem

    def get_resumo(self):
        return f"Tipo: {self.tipo} | Aluguel base: R$ {self.valor_base:.2f}"


# Classe para Apartamento - herda de Imovel
class Apartamento(Imovel):
    def __init__(self, quartos, tem_crianca, tem_garagem):
        super().__init__("Apartamento")
        self.quartos = quartos
        self.tem_crianca = tem_crianca
        self.tem_garagem = tem_garagem

        # Valor base: R$700
        self.valor_base = 700.00 

        # 2 quartos tem acréscimo de R$200
        if quartos == 2:
            self.valor_base += 200.00

        # Desconto de 5% para quem não tem criança
        if not tem_crianca:
            self.desconto = self.valor_base * 0.05
            self.valor_base -= self.desconto
        else:
            self.desconto = 0.0

        # Adiciona garagem se solicitado
        if tem_garagem:
            self.adicionar_garagem()

    def calcular_aluguel(self):
        return self.valor_base + self.valor_garagem

    def get_resumo(self):
        resumo = f"Tipo: Apartamento | Quartos: {self.quartos}"
        if self.desconto > 0:
            resumo += f" | Desconto (sem crianças): R$ {self.desconto:.2f}"
        if self.tem_garagem:
            resumo += f" | Garagem: R$ {self.valor_garagem:.2f}"
        return resumo


# Classe para Casa - herda de Imovel
class Casa(Imovel):
    def __init__(self, quartos, tem_garagem):
        super().__init__("Casa")
        self.quartos = quartos
        self.tem_garagem = tem_garagem

        # Valor base: R$900
        self.valor_base = 900.00 

        # 2 quartos tem acréscimo de R$250
        if quartos == 2:
            self.valor_base += 250.00

        # Adiciona garagem se solicitado
        if tem_garagem:
            self.adicionar_garagem()

    def calcular_aluguel(self):
        return self.valor_base + self.valor_garagem

    def get_resumo(self):
        resumo = f"Tipo: Casa | Quartos: {self.quartos}"
        if self.tem_garagem:
            resumo += f" | Garagem: R$ {self.valor_garagem:.2f}"
        return resumo


# Classe para Estúdio - herda de Imovel
class Estudio(Imovel):
    def __init__(self, vagas_extras):
        super().__init__("Estúdio")
        self.valor_base = 1200.00
        self.vagas_extras = vagas_extras

        # 2 vagas fixas = R$250, vagas extras = R$60 cada
        if vagas_extras >= 0:
            self.valor_estacionamento = 250.00 + (vagas_extras * 60.00)
        else:
            self.valor_estacionamento = 0.0

    def calcular_aluguel(self):
        return self.valor_base + self.valor_estacionamento

    def get_valor_extras(self):
        return self.valor_estacionamento

    def get_resumo(self):
        resumo = f"Tipo: Estúdio"
        if self.valor_estacionamento > 0:
            total_vagas = 2 + self.vagas_extras
            resumo += f" | Estacionamento ({total_vagas} vagas): R$ {self.valor_estacionamento:.2f}"
        return resumo
