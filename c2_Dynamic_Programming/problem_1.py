class PacoteMochila:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

class Mochila01Dinamica:
    def __init__(self):
        pass

    def resolver_mochila_01(self, pesos, valores, capacidade, n_itens):
        # Cria os objetos PacoteMochila
        pacotes = [PacoteMochila(pesos[i], valores[i]) for i in range(n_itens)]

        # Cria a tabela dp (n_itens+1) x (capacidade+1)
        # dp[i][c] = valor máximo usando os primeiros i itens com capacidade c
        dp = [[0]*(capacidade+1) for _ in range(n_itens+1)]

        # Preenche a tabela dp
        for i in range(1, n_itens+1):
            peso_atual = pacotes[i-1].peso
            valor_atual = pacotes[i-1].valor
            for c in range(1, capacidade+1):
                # Se não incluir o item i
                dp[i][c] = dp[i-1][c]

                # Se incluir o item i (se couber)
                if peso_atual <= c:
                    dp[i][c] = max(dp[i][c], dp[i-1][c - peso_atual] + valor_atual)

        # O valor máximo está em dp[n_itens][capacidade]
        valor_maximo = dp[n_itens][capacidade]

        # (Opcional) Recuperação dos itens escolhidos:
        itens_escolhidos = []
        c = capacidade
        for i in range(n_itens, 0, -1):
            if dp[i][c] != dp[i-1][c]:
                # Significa que o item i foi incluído
                itens_escolhidos.append(i-1)
                c -= pacotes[i-1].peso

        # Imprime os itens escolhidos (opcional)
        print("Itens escolhidos:")
        for i in reversed(itens_escolhidos):
            print(f"Item {i} - Peso: {pacotes[i].peso}, Valor: {pacotes[i].valor}")

        print(f"Valor Máximo: {valor_maximo}")
        return valor_maximo


if __name__ == "__main__":
    # Pesos e valores dos itens
    pesos = [15, 10, 2, 4]
    valores = [30, 25, 2, 6]

    # Quantidade de itens
    n = len(pesos)

    # Capacidade máxima
    capacidade = 37

    proc = Mochila01Dinamica()
    proc.resolver_mochila_01(pesos, valores, capacidade, n)
