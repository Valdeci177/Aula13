class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            litros_disponiveis = self.quantidade_combustivel
            self.quantidade_combustivel = 0
            return litros_disponiveis

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_combustivel:
            valor_pagar = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            return valor_pagar
        else:
            litros_disponiveis = self.quantidade_combustivel
            self.quantidade_combustivel = 0
            return litros_disponiveis * self.valor_litro

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade


# Exemplo de uso da classe BombaCombustivel
bomba1 = BombaCombustivel("Gasolina", 5.50, 1000)
print("Abastecidos", bomba1.abastecer_por_valor(55), "litros")
print("Valor a ser pago:", bomba1.abastecer_por_litro(20), "reais")
print("Quantidade de combustível restante:", bomba1.quantidade_combustivel, "litros")
bomba1.alterar_valor(5.70)
bomba1.alterar_combustivel("Diesel")
bomba1.alterar_quantidade_combustivel(1500)
print("Novo valor do litro:", bomba1.valor_litro)
print("Novo tipo de combustível:", bomba1.tipo_combustivel)
print("Nova quantidade de combustível:", bomba1.quantidade_combustivel, "litros")