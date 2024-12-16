# test_cases.py
import unittest
from problem_1 import Item, BranchAndBound

class TestKnapsackProblemBandB(unittest.TestCase):
    def test_case_1(self):
        """
        Caso básico: capacidade suficiente para alguns itens.
        Espera-se selecionar os itens com índices [1, 2], totalizando valor 220.
        """
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50

        # Criação dos itens
        items = [Item(value=val, weight=wt) for val, wt in zip(values, weights)]
        
        # Instanciação do BranchAndBound
        bnb = BranchAndBound(items, capacity)
        resultValue, selectedItem = bnb.KnapsackBandB()

        # Valores esperados
        expectedValue = 220
        expectedSelected = [1, 2]

        # Verificações
        self.assertEqual(resultValue, expectedValue, f"Expected value {expectedValue}, got {resultValue}")
        self.assertEqual(sorted(selectedItem), sorted(expectedSelected), f"Expected items {expectedSelected}, got {selectedItem}")

        print(f"Test case 1 passed! Soluções encontradas: {resultValue}")

    def test_case_2(self):
        """
        Caso com capacidade insuficiente.
        Espera-se não selecionar nenhum item, totalizando valor 0.
        """
        values = [10, 20, 30]
        weights = [5, 10, 15]
        capacity = 0

        # Criação dos itens
        items = [Item(value=val, weight=wt) for val, wt in zip(values, weights)]
        
        # Instanciação do BranchAndBound
        bnb = BranchAndBound(items, capacity)
        resultValue, selectedItem = bnb.KnapsackBandB()

        # Valores esperados
        expectedValue = 0
        expectedSelected = []

        # Verificações
        self.assertEqual(resultValue, expectedValue, f"Expected value {expectedValue}, got {resultValue}")
        self.assertEqual(selectedItem, expectedSelected, f"Expected items {expectedSelected}, got {selectedItem}")

        print(f"Test case 2 passed! Soluções encontradas: {resultValue}")

    def test_case_3(self):
        """
        Caso onde todos os itens podem ser escolhidos.
        Espera-se selecionar todos os itens, totalizando valor 100.
        """
        values = [10, 40, 50]
        weights = [1, 2, 3]
        capacity = 6

        # Criação dos itens
        items = [Item(value=val, weight=wt) for val, wt in zip(values, weights)]
        
        # Instanciação do BranchAndBound
        bnb = BranchAndBound(items, capacity)
        resultValue, selectedItem = bnb.KnapsackBandB()

        # Valores esperados
        expectedValue = 100
        expectedSelected = [0, 1, 2]

        # Verificações
        self.assertEqual(resultValue, expectedValue, f"Expected value {expectedValue}, got {resultValue}")
        self.assertEqual(sorted(selectedItem), sorted(expectedSelected), f"Expected items {expectedSelected}, got {selectedItem}")

        print(f"Test case 3 passed! Soluções encontradas: {resultValue}")

if __name__ == '__main__':
    unittest.main()
