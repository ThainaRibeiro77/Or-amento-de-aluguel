# Sistema de Orçamento de Aluguel - Imobiliária R.M 🏢

Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em **Python** para automatizar a geração de orçamentos de locação de imóveis (Apartamentos, Casas e Estúdios). O sistema foi construído aplicando os princípios da **Programação Orientada a Objetos (POO)**.

## 🚀 Funcionalidades

- **Cálculo Personalizado:** Precificação baseada no tipo de imóvel, quantidade de quartos e adição de vagas de garagem ou estacionamento.
- **Regras de Negócio Aplicadas:** Inclusão automática de taxas extras e aplicação de descontos (ex: desconto para apartamentos sem crianças).
- **Gestão de Contrato:** Processamento do valor do contrato imobiliário (R$ 2.000,00) com opção de parcelamento em até 5 vezes.
- **Exportação de Dados:** Geração automática de um arquivo `.csv` contendo o detalhamento financeiro das 12 parcelas anuais, formatado para o padrão brasileiro.

## 💻 Estrutura do Projeto

O código está modularizado em três arquivos principais para separar as responsabilidades:

- `main.py`: Ponto de entrada do sistema. Gerencia os menus interativos, coleta de dados do usuário e tratamento de erros de validação.
- `imovel.py`: Contém a classe base abstrata `Imovel` e suas subclasses (`Apartamento`, `Casa`, `Estudio`), encapsulando os atributos e as lógicas de cálculo (polimorfismo).
- `orcamento.py`: Responsável por consolidar os dados do imóvel escolhido e do contrato, além de executar a exportação do relatório financeiro final em CSV.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Bibliotecas nativas: `csv`, `os`, `datetime`

   
